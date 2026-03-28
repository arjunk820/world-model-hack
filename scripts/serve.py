#!/usr/bin/env python3
"""Simple local server - needed so GLB files load without CORS issues."""
import http.server, socketserver, os

PORT = 8080
os.chdir(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class Handler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Cross-Origin-Opener-Policy', 'same-origin')
        self.send_header('Cross-Origin-Embedder-Policy', 'require-corp')
        super().end_headers()

with socketserver.TCPServer(('', PORT), Handler) as httpd:
    print(f'Serving at http://localhost:{PORT}')
    print(f'Open: http://localhost:{PORT}/pipeline/simulate.html')
    httpd.serve_forever()
