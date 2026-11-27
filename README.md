# 桂少聪 · 3D 个人主页（igloo-clone）

基于 Three.js / WebGL 的 4 场景 3D 个人主页与作品集。

- **线上地址**：https://congcong-gui.netlify.app
- **GitHub 仓库**：`6gsc/igloo-clone`（私有仓库，`main` 分支）

## 目录结构

- `index.html` / `index.before-v7.html` — 入口 HTML 及构建模板
- `tools/build_plan_v8.py` — 核心构建脚本（文案、项目卡片、详情页、交互逻辑均在此维护）
- `tools/test_plan_v8.cjs` — Playwright 自动化回归脚本
- `assets/App3D-aurora-preview-v6.js` / `assets/index-aurora-preview-v6.js` — v6 基础包（由 `build_plan_v8.py` 注入补丁生成 `v8`）
- `assets/App3D-aurora-preview-v8.js` / `assets/index-aurora-preview-v8.js` — 构建生成的线上版本包
- `rebuild_font.sh` — MSDF 中英文字体图集重建脚本
- `serve.sh` / `nocache_server.py` — 本地无缓存预览服务
- `deploy.sh` — 一键打包 `deploy-dist/` 并发布到 Netlify 生产环境

## 本地预览

```bash
./serve.sh            # 默认 8791 端口
./serve.sh 9000       # 自定义端口
```

浏览器打开 `http://127.0.0.1:8791/`。

## 修改文案与重新构建

1. 编辑 `tools/build_plan_v8.py` 中的文案或配置。
2. 重新生成 `v8` 产物：
   ```bash
   python3 tools/build_plan_v8.py
   ```
3. 如果新增了此前字体图集中没有的中文字符，运行字体重建（需先安装 `pip3 install fonttools brotly`）：
   ```bash
   ./rebuild_font.sh
   ```
4. 本地启动 `./serve.sh` 预览确认无误。

## 多设备协作更新流程

1. **首次在新设备拉取**（需登录 GitHub 账号 `6gsc` 或被添加为仓库 Collaborator）：
   ```bash
   git clone https://github.com/6gsc/igloo-clone.git
   cd igloo-clone
   ```
2. **每次修改前先同步最新代码**：
   ```bash
   git pull origin main
   ```
3. 修改 `tools/build_plan_v8.py`、运行 `python3 tools/build_plan_v8.py` 并本地预览验证。
4. **提交并推送到 GitHub**：
   ```bash
   git add <改动文件>
   git commit -m "说明本次修改内容"
   git push origin main
   ```

## 发布更新到 Netlify

在新设备上首次发布前，先登录同一 Netlify 账号：

```bash
npx netlify-cli login
```

之后直接运行脚本即可构建干净产物并发布到 https://congcong-gui.netlify.app ：

```bash
./deploy.sh "本次更新说明"
```
