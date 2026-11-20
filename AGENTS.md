# igloo-clone 工作守则

## 修改前必须建回退存档（硬性要求）

凡修改本目录内任何文件（含 assets/ 下的模型、贴图、bundle），动手前必须完成：

1. 首次修改前：`git init` + 全量 `git add -A` + `git commit` 作为基线（若尚未 init）；同时打一个全量快照 `tar --exclude '.git' -czf ../igloo-clone-backup-$(date +%Y%m%d-%H%M).tar.gz .` 存到上级目录。
2. 每个改动：只在新文件上作业 + 改配置指向，不覆盖原文件；确需覆盖时先留 `.bak`。
3. 每个改动经过浏览器验证（127.0.0.1:8791）通过后才 `git commit`，commit 信息写清改了什么。
4. 回退方式：`git checkout -- <文件>` 或解包快照；不允许在无存档状态下继续改动。

## 其他约束

- 文字内容（宣言、版权、作品占位、链接）已替换完成，不要动。
- 站点结构、山体、雪、烟、plexus、相机/滚动逻辑保持不变。
- 本地服务：`python3 nocache_server.py 8791`（可能已在运行）。
