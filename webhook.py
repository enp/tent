#!/usr/bin/env python3

import json

from http.server import HTTPServer, BaseHTTPRequestHandler

class WebHookHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        self.send_response(200)
        self.end_headers()
        self.data = json.loads(self.rfile.read(int(self.headers['Content-Length'])))
        print(self.data)

httpd = HTTPServer(('0.0.0.0', 18202), WebHookHandler)
httpd.serve_forever()
