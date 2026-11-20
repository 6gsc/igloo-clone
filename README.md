# igloo.inc 本地复刻

https://www.igloo.inc/ 的完整本地镜像（Three.js WebGL 沉浸式 3D 站点，abeto.co 制作）。
资源全部本地化，无任何对 igloo.inc 的外部请求。

## 运行

```bash
./serve.sh            # 默认 8791 端口
./serve.sh 9000       # 自定义端口
```

然后浏览器打开 http://127.0.0.1:8791/

## 目录结构

- `index.html` — 入口，已改为本地路径
- `assets/` — 完整镜像（109 个文件，22MB）：
  - `index-2e130bc1.js` / `App3D-d68cb154.js` — 主 bundle（内部 `https://www.igloo.inc/` 已替换为同源路径 `/`）
  - `audioworker / msdfworker / bitmapworker / exrworker` — 4 个 Web Worker
  - `images/` — ktx2/exr/png 纹理（igloo 场景、cubes、体积云、UI 等）
  - `geometries/` — draco 压缩网格（.drc）
  - `audio/` — 17 个 ogg 音效
  - `fonts/` — IBM Plex Mono woff/woff2 + MSDF 字形纹理
  - `libs/` — basis / draco 转码 wasm

## 与原版的一致性验证

- 本地 100 个网络请求全部 200/304，0 个外部请求，0 个 404
- DOM 结构与原站一致（`#app > #webgl`），控制台无报错
- 资源完整性：bundle 引用的 80 个资源名全部本地命中
- `shots/` 内保留了本地与原站的 1440x900 对比截图

重新抓取资源（站点更新后）：`./download.sh`
