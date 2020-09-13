#!/usr/bin/env python3

import json, subprocess

from http.server import HTTPServer, BaseHTTPRequestHandler

class WebHookHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        self.send_response(200)
        self.end_headers()
        delivery = self.headers['X-GitHub-Delivery']
        data = json.loads(self.rfile.read(int(self.headers['Content-Length'])))
        repo_map = { 'enp/tent:application': 'enp/tent:metadata' }
        src_repo = '{}:{}'.format(data['repository']['full_name'], data['ref'].split('/')[-1])
        dst_repo = repo_map[src_repo]
        subprocess.call(['./webhook.sh', delivery, dst_repo.split(':')[0], dst_repo.split(':')[1]])

httpd = HTTPServer(('0.0.0.0', 18202), WebHookHandler)
httpd.serve_forever()
