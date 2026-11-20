#!/usr/bin/env python3
"""no-cache 静态服务器 + SPA 路由回退。
所有响应带 Cache-Control: no-store；不存在的路径回退 index.html（与原站 SPA 行为一致）。"""
import sys
import os
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer

ROOT = os.path.dirname(os.path.abspath(__file__))

class NoCacheHandler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=ROOT, **kwargs)

    def end_headers(self):
        self.send_header('Cache-Control', 'no-store, no-cache, must-revalidate')
        self.send_header('Pragma', 'no-cache')
        super().end_headers()

    def send_head(self):
        # SPA 回退：路径不存在或指向目录时回 index.html
        path = self.translate_path(self.path)
        if not os.path.exists(path) or os.path.isdir(path) and not os.path.exists(os.path.join(path, 'index.html')):
            if not self.path.startswith('/assets/'):
                self.path = '/index.html'
        return super().send_head()

if __name__ == '__main__':
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 8791
    print(f'serving (no-cache + SPA fallback) on http://127.0.0.1:{port}/')
    ThreadingHTTPServer(('127.0.0.1', port), NoCacheHandler).serve_forever()
