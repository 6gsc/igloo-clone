#!/bin/bash
# Mirror igloo.inc static assets into ./ (preserving /assets structure)
set -u
BASE="https://www.igloo.inc"
UA="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0 Safari/537.36"
cd "$(dirname "$0")"

fetch() {
  local path="$1"
  local out=".${path}"
  mkdir -p "$(dirname "$out")"
  if [ -s "$out" ]; then return 0; fi
  local code
  code=$(curl -sL -A "$UA" --retry 3 --retry-delay 1 -o "$out" -w "%{http_code}" "$BASE$path")
  if [ "$code" != "200" ]; then
    echo "FAIL $code $path"
    rm -f "$out"
    return 1
  fi
  echo "OK   $path"
}

# entry + bundles + workers
for p in \
  / \
  /assets/index-2e130bc1.js \
  /assets/App3D-d68cb154.js \
  /assets/audioworker-036a09db.js \
  /assets/msdfworker-ac346fa7.js \
  /assets/bitmapworker-046527f8.js \
  /assets/exrworker-41cbee65.js \
  /assets/favicon32-af94112f.png \
  /assets/favicon16-9e4401be.png \
  /assets/images/social.jpg \
  /assets/IBMPlexMono-Medium-897c8c30.woff2 \
  /assets/IBMPlexMono-Medium-1e253194.woff \
  /assets/IBMPlexMono-Regular-d3034935.woff2 \
  /assets/IBMPlexMono-Regular-419d45f6.woff \
  ; do fetch "$p"; done

# fonts (msdf json)
for f in IBMPlexMono-Medium IBMPlexMono-Regular; do
  fetch "/assets/fonts/$f.json"
done

# libs
for f in \
  basis/basis_transcoder.js basis/basis_transcoder.wasm \
  draco/draco_wasm_wrapper.js draco/draco_decoder.wasm draco/draco_decoder.js \
  ; do fetch "/assets/libs/$f"; done

# geometries
for f in \
  mountain.drc ground.drc igloo.drc intro_particles.drc blurrytext.drc \
  shattered_ring2.drc floor.drc blurrytext_cylinder.drc smoke_trail.drc \
  shattered_ring_smoke.drc ceilingsmoke.drc pudgy.drc overpass_logo.drc shattered_ring.drc \
  igloo/igloo_cage.drc igloo/igloo_outline.drc igloo/patch.drc \
  cubes/background_shapes.drc cubes/cube1.drc cubes/cube3.drc \
  ; do fetch "/assets/geometries/$f"; done

# images
for f in \
  scroll-datatexture.ktx2 frost-datatexture.ktx2 wind_noise.ktx2 clouds_noise.ktx2 \
  bokeh.ktx2 mosaic.ktx2 shapes_blurred.ktx2 pudgy_dark_color.ktx2 caustics.ktx2 \
  overpass_logo_dark_color.ktx2 floor_color.ktx2 numbers-datatexture.ktx2 \
  shattered_ring2_color.ktx2 shattered_ring2_ao.ktx2 shattered_ring_color.ktx2 shattered_ring_ao.ktx2 \
  perlin-datatexture.ktx2 perlin-datatexture.png \
  noises/blue-8-128-rgb.ktx2 \
  ui/logo-datatexture.ktx2 ui/sound-datatexture.ktx2 ui/close-datatexture.ktx2 \
  ui/arrow-datatexture.ktx2 ui/visit-datatexture.ktx2 \
  cubes/dot_pattern.ktx2 cubes/cube_scene.ktx2 cubes/blurrytext_atlas.ktx2 cubes/bg.png \
  cubes/advect.png cubes_env.exr cubes/cube3_roughness.ktx2 cubes/cube3_normal.ktx2 \
  cubes/pudgy_color.ktx2 cubes/cube1_roughness.ktx2 cubes/cube1_normal.ktx2 \
  cubes/overpass_logo_color.ktx2 \
  igloo/triangles_tiling.ktx2 igloo/igloo_scene.ktx2 igloo/mountain_color.ktx2 \
  igloo/ground_sansigloo_color.ktx2 igloo/numbers.ktx2 igloo/ground_color.ktx2 \
  igloo/ground_glow.ktx2 igloo/igloo_color.ktx2 igloo/igloo_exploded_color.ktx2 \
  volumes/peachesbody_64.ktx2 volumes/x_64.ktx2 volumes/medium_32.ktx2 \
  uv/uvchecker-srgb.ktx2 uv/uvchecker-srgb.png \
  ; do fetch "/assets/images/$f"; done

# fonts datatexture
fetch "/assets/fonts/IBMPlexMono-Medium-datatexture.ktx2"

# audio
for f in \
  music-highq.ogg room.ogg wind.ogg igloo.ogg beeps.ogg beeps2.ogg beeps3.ogg \
  click-project.ogg enter-project.ogg leave-project.ogg shard.ogg project-text.ogg \
  circles.ogg particles.ogg logo.ogg ui-long.ogg ui-short.ogg manifesto.ogg \
  ; do fetch "/assets/audio/$f"; done

echo "--- done ---"
du -sh .
