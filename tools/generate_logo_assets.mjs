import assert from 'node:assert/strict';
import { createRequire } from 'node:module';
import { readFile, writeFile, mkdtemp, rm } from 'node:fs/promises';
import { tmpdir } from 'node:os';
import { dirname, join, resolve } from 'node:path';
import { pathToFileURL } from 'node:url';
import { deflateSync } from 'node:zlib';
import { spawnSync } from 'node:child_process';

const root = resolve(import.meta.dirname, '..');
const dependencyRoot = process.env.LOGO_DEPS;
assert(dependencyRoot, 'Set LOGO_DEPS to the isolated dependency directory.');
const require = createRequire(join(dependencyRoot, 'package.json'));
const threeRoot = dirname(dirname(require.resolve('three')));
const [{ SVGLoader }, { ExtrudeGeometry }, { JSDOM }, draco] = await Promise.all([
  import(pathToFileURL(join(threeRoot, 'examples/jsm/loaders/SVGLoader.js'))),
  import(pathToFileURL(join(threeRoot, 'build/three.module.js'))),
  import(pathToFileURL(require.resolve('jsdom'))),
  import(pathToFileURL(require.resolve('draco3dgltf')))
]);
globalThis.DOMParser = new JSDOM('').window.DOMParser;

const specs = [
  { name: 'inovance_logo', svg: '../个人作品集网站/assets/logos/inovance.svg', width: 1.3,
    colorPath: 'assets/images/cubes/inovance_logo_color.ktx2', darkPath: 'assets/images/inovance_logo_dark_color.ktx2',
    bright: ['#0094E7', '#5A5858'], dark: ['#073759', '#27313A'] },
  { name: 'nio_logo', svg: '../个人作品集网站/assets/logos/nio.svg', width: 1.35,
    colorPath: 'assets/images/cubes/nio_logo_color.ktx2', darkPath: 'assets/images/nio_logo_dark_color.ktx2',
    bright: ['#F5FAFF', '#F5FAFF'], dark: ['#173348', '#173348'] }
];

function newGeometry(shape, name) {
  const depth = name === 'nio_logo' ? 8 : 6;
  return new ExtrudeGeometry(shape, {
    depth,
    bevelEnabled: true,
    bevelThickness: depth * 0.08,
    bevelSize: depth * 0.06,
    bevelSegments: 2,
    curveSegments: 12
  });
}

function mergedArray(chunks) {
  const length = chunks.reduce((sum, chunk) => sum + chunk.length, 0);
  const result = new Float32Array(length);
  let offset = 0;
  for (const chunk of chunks) { result.set(chunk, offset); offset += chunk.length; }
  return result;
}

export function buildLogoGeometry(svgText, name, width) {
  const paths = new SVGLoader().parse(svgText).paths;
  const parts = paths.flatMap(path => SVGLoader.createShapes(path).map(shape => ({
    kind: name === 'nio_logo' ? 'nio' : path.userData.node.id.endsWith('_icon_logo') ? 'english' : 'chinese',
    geometry: newGeometry(shape, name)
  })));
  assert(parts.length, `${name}: SVG has no extrudable paths`);

  const boxes = new Map();
  for (const part of parts) {
    part.geometry.computeBoundingBox();
    const box = boxes.get(part.kind) ?? { min: [Infinity, Infinity, Infinity], max: [-Infinity, -Infinity, -Infinity] };
    for (let axis = 0; axis < 3; axis++) {
      box.min[axis] = Math.min(box.min[axis], part.geometry.boundingBox.min.getComponent(axis));
      box.max[axis] = Math.max(box.max[axis], part.geometry.boundingBox.max.getComponent(axis));
    }
    boxes.set(part.kind, box);
  }
  if (name === 'nio_logo') {
    const all = { min: [Infinity, Infinity, Infinity], max: [-Infinity, -Infinity, -Infinity] };
    for (const box of boxes.values()) for (let axis = 0; axis < 3; axis++) {
      all.min[axis] = Math.min(all.min[axis], box.min[axis]);
      all.max[axis] = Math.max(all.max[axis], box.max[axis]);
    }
    boxes.set('nio', all);
  }
  const chunks = { position: [], normal: [], uv: [], indices: [] };
  let vertexOffset = 0;
  for (const part of parts) {
    const box = boxes.get(part.kind);
    const scale = width / (box.max[0] - box.min[0]);
    const height = (box.max[1] - box.min[1]) * scale;
    const gap = name === 'inovance_logo' ? width * 0.09 : 0;
    const yOffset = part.kind === 'english' ? (height + gap) / 2 : part.kind === 'chinese' ? -(height + gap) / 2 : 0;
    const geo = part.geometry;
    geo.rotateX(Math.PI);
    const position = geo.getAttribute('position');
    const uvV = part.kind === 'english' ? 0.25 : part.kind === 'chinese' ? 0.75 : 0.5;
    const transformed = new Float32Array(position.count * 3);
    const projected = new Float32Array(position.count * 2);
    for (let i = 0; i < position.count; i++) {
      const x = (position.getX(i) - (box.min[0] + box.max[0]) / 2) * scale;
      const y = (position.getY(i) + (box.min[1] + box.max[1]) / 2) * scale + yOffset;
      const z = (position.getZ(i) + (box.min[2] + box.max[2]) / 2) * scale;
      transformed.set([x, y, z], i * 3);
      projected.set([(x / width) + 0.5, uvV], i * 2);
    }
    chunks.position.push(transformed);
    chunks.normal.push(new Float32Array(geo.getAttribute('normal').array));
    chunks.uv.push(projected);
    const index = geo.index;
    const indices = new Uint32Array(index?.count ?? position.count);
    for (let i = 0; i < indices.length; i++) indices[i] = (index ? index.getX(i) : i) + vertexOffset;
    chunks.indices.push(indices);
    vertexOffset += position.count;
    geo.dispose();
  }

  const positions = mergedArray(chunks.position);
  const center = [0, 1, 2].map(axis => {
    let min = Infinity, max = -Infinity;
    for (let i = axis; i < positions.length; i += 3) { min = Math.min(min, positions[i]); max = Math.max(max, positions[i]); }
    return (min + max) / 2;
  });
  for (let i = 0; i < positions.length; i++) positions[i] -= center[i % 3];
  return {
    position: positions,
    normal: mergedArray(chunks.normal),
    uv: mergedArray(chunks.uv),
    indices: Uint32Array.from(chunks.indices.flatMap(chunk => Array.from(chunk))),
    bounds: [0, 1, 2].map(axis => {
      let min = Infinity, max = -Infinity;
      for (let i = axis; i < positions.length; i += 3) { min = Math.min(min, positions[i]); max = Math.max(max, positions[i]); }
      return max - min;
    }),
    vertices: positions.length / 3,
    faces: chunks.indices.reduce((sum, chunk) => sum + chunk.length, 0) / 3
  };
}

export async function encodeDraco(mesh, outputPath) {
  const module = await draco.createEncoderModule({});
  const encoder = new module.Encoder(), builder = new module.MeshBuilder(), geometry = new module.Mesh();
  const vertexCount = mesh.position.length / 3, faceCount = mesh.indices.length / 3;
  builder.AddFacesToMesh(geometry, faceCount, mesh.indices);
  const ids = [
    builder.AddFloatAttributeToMesh(geometry, module.POSITION, vertexCount, 3, mesh.position),
    builder.AddFloatAttributeToMesh(geometry, module.NORMAL, vertexCount, 3, mesh.normal),
    builder.AddFloatAttributeToMesh(geometry, module.TEX_COORD, vertexCount, 2, mesh.uv)
  ];
  assert(ids.every(id => id >= 0), `Could not add Draco attributes: ${ids}`);
  encoder.SetSpeedOptions(5, 5);
  encoder.SetAttributeQuantization(module.POSITION, 20);
  encoder.SetAttributeQuantization(module.NORMAL, 16);
  encoder.SetAttributeQuantization(module.TEX_COORD, 16);
  const encoded = new module.DracoInt8Array();
  const length = encoder.EncodeMeshToDracoBuffer(geometry, encoded);
  assert(length > 0, 'Draco encoding failed');
  const raw = Buffer.alloc(length);
  for (let i = 0; i < length; i++) raw[i] = encoded.GetValue(i) & 255;
  const info = Buffer.from(JSON.stringify({ type: 0, attributes: [['position', 7], ['normal', 7], ['uv', 7]], userData: {} }));
  const header = Buffer.alloc(4);
  header.writeUInt32LE(info.length);
  await writeFile(outputPath, Buffer.concat([header, info, raw]));
  module.destroy(encoded); module.destroy(geometry); module.destroy(builder); module.destroy(encoder);
  return { ids };
}

export async function inspectDraco(filePath) {
  const module = await draco.createDecoderModule({}), bytes = await readFile(filePath);
  const infoLength = bytes.readUInt32LE(0), info = JSON.parse(bytes.subarray(4, 4 + infoLength));
  const decoder = new module.Decoder(), buffer = new module.DecoderBuffer();
  const raw = bytes.subarray(4 + infoLength);
  buffer.Init(new Int8Array(raw.buffer, raw.byteOffset, raw.byteLength), raw.length);
  const mesh = new module.Mesh(), status = decoder.DecodeBufferToMesh(buffer, mesh);
  assert(status.ok(), status.error_msg());
  const result = { info, vertices: mesh.num_points(), faces: mesh.num_faces(), attributes: [] };
  for (let i = 0; i < info.attributes.length; i++) {
    const attribute = decoder.GetAttributeByUniqueId(mesh, i);
    assert(attribute.ptr, `Missing attribute ${info.attributes[i][0]} at unique ID ${i}`);
    result.attributes.push({ name: info.attributes[i][0], components: attribute.num_components() });
  }
  module.destroy(mesh); module.destroy(buffer); module.destroy(decoder);
  return result;
}

function pngChunk(type, payload) {
  const name = Buffer.from(type), crcInput = Buffer.concat([name, payload]);
  let crc = 0xffffffff;
  for (const byte of crcInput) {
    crc ^= byte;
    for (let bit = 0; bit < 8; bit++) crc = (crc >>> 1) ^ (crc & 1 ? 0xedb88320 : 0);
  }
  const chunk = Buffer.alloc(12 + payload.length);
  chunk.writeUInt32BE(payload.length, 0); name.copy(chunk, 4); payload.copy(chunk, 8);
  chunk.writeUInt32BE((crc ^ 0xffffffff) >>> 0, 8 + payload.length);
  return chunk;
}

export async function writeColorTexture(path, topHex, bottomHex = topHex) {
  const width = 1024, height = 1024;
  const parse = color => Buffer.from(color.slice(1).match(/.{2}/g).map(part => parseInt(part, 16)));
  const top = parse(topHex), bottom = parse(bottomHex);
  const scanlines = Buffer.alloc(height * (width * 4 + 1));
  for (let y = 0; y < height; y++) {
    const row = y * (width * 4 + 1), color = y < height / 2 ? top : bottom;
    for (let x = 0; x < width; x++) {
      const offset = row + 1 + x * 4;
      scanlines[offset] = color[0]; scanlines[offset + 1] = color[1]; scanlines[offset + 2] = color[2]; scanlines[offset + 3] = 255;
    }
  }
  const header = Buffer.alloc(13);
  header.writeUInt32BE(width, 0); header.writeUInt32BE(height, 4); header.set([8, 6, 0, 0, 0], 8);
  await writeFile(path, Buffer.concat([
    Buffer.from([137, 80, 78, 71, 13, 10, 26, 10]), pngChunk('IHDR', header),
    pngChunk('IDAT', deflateSync(scanlines)), pngChunk('IEND', Buffer.alloc(0))
  ]));
}

export async function generateAll(name) {
  const selected = name ? specs.filter(spec => spec.name === name) : specs;
  assert(selected.length, `Unknown logo: ${name}`);
  for (const spec of selected) {
    const mesh = buildLogoGeometry(await readFile(resolve(root, spec.svg), 'utf8'), spec.name, spec.width);
    const drcPath = join(root, 'assets/geometries', `${spec.name}.drc`);
    await encodeDraco(mesh, drcPath);
    const check = await inspectDraco(drcPath);
    assert(check.vertices > 0 && check.vertices <= mesh.vertices);
    assert.equal(check.faces, mesh.faces);
    assert.deepEqual(check.attributes.map(attr => [attr.name, attr.components]), [['position', 3], ['normal', 3], ['uv', 2]]);
    assert(mesh.bounds.every(value => value > 0 && value < 1.6), `${spec.name}: invalid bounds ${mesh.bounds}`);
    const outputDir = await mkdtemp(join(tmpdir(), 'igloo-logo-'));
    try {
      for (const [relativePath, colors] of [[spec.colorPath, spec.bright], [spec.darkPath, spec.dark]]) {
        const pngPath = join(outputDir, 'color.png');
        const rawPath = join(outputDir, 'raw.ktx2');
        const ktxPath = join(root, relativePath);
        await writeColorTexture(pngPath, ...colors);
        for (const [tool, args] of [
          ['toktx', ['--t2', '--assign_oetf', 'srgb', '--genmipmap', rawPath, pngPath]],
          ['ktxsc', ['--encode', 'etc1s', '--qlevel', '200', '-o', ktxPath, rawPath]]
        ]) {
          const result = spawnSync(join(root, 'tools/ktx/bin', tool), args, { encoding: 'utf8' });
          assert.equal(result.status, 0, result.error ?? (result.stderr || result.stdout));
        }
        const info = spawnSync(join(root, 'tools/ktx/bin/ktxinfo'), [ktxPath], { encoding: 'utf8' });
        assert.equal(info.status, 0, info.stderr || info.stdout);
        assert.match(info.stdout, /KTX_SS_BASIS_LZ/);
        assert.match(info.stdout, /Transfer: KHR_DF_TRANSFER_SRGB/);
      }
    } finally {
      await rm(outputDir, { recursive: true, force: true });
    }
    process.stdout.write(`${spec.name}: ${mesh.vertices} vertices, ${mesh.faces} faces, ${mesh.bounds.map(n => n.toFixed(3)).join(' × ')}\n`);
  }
}

if (process.argv[1] && resolve(process.argv[1]) === resolve(import.meta.filename)) await generateAll();
