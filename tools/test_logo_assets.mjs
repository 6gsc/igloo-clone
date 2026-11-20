import assert from 'node:assert/strict';
import { test } from 'node:test';
import { buildLogoGeometry, encodeDraco, inspectDraco } from './generate_logo_assets.mjs';

const logoSvg = `<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20"><path id="icon-logo02_icon_logo" fill="#0094e7" d="M1 1H9V9H1Z"/><path id="icon-logo02_Vector" fill="#5a5858" d="M11 11H19V19H11Z"/></svg>`;

test('extrudes and centers SVG paths with matching position, normal and UV streams', () => {
  const mesh = buildLogoGeometry(logoSvg, 'inovance_logo', 1.3);
  assert.equal(mesh.position.length, mesh.vertices * 3);
  assert.equal(mesh.normal.length, mesh.vertices * 3);
  assert.equal(mesh.uv.length, mesh.vertices * 2);
  assert.equal(mesh.indices.length, mesh.faces * 3);
  assert(mesh.faces > 0);
  for (let axis = 0; axis < 3; axis++) {
    const values = Array.from({ length: mesh.vertices }, (_, i) => mesh.position[i * 3 + axis]);
    assert(Math.abs((Math.min(...values) + Math.max(...values)) / 2) < 1e-5);
  }
});

test('Draco file header preserves loader attribute order and round-trips mesh counts', async () => {
  const mesh = buildLogoGeometry(logoSvg, 'nio_logo', 1.35);
  const path = `/tmp/igloo-logo-${process.pid}.drc`;
  const { ids } = await encodeDraco(mesh, path);
  const decoded = await inspectDraco(path);
  assert.deepEqual(ids.map(id => id >= 0), [true, true, true]);
  assert.deepEqual(decoded.info.attributes, [['position', 7], ['normal', 7], ['uv', 7]]);
  assert(decoded.vertices > 0 && decoded.vertices <= mesh.vertices);
  assert.equal(decoded.faces, mesh.faces);
  assert.deepEqual(decoded.attributes.map(attribute => attribute.components), [3, 3, 2]);
});
