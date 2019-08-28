# -*- coding:utf-8 -*-
from http.server import HTTPServer, BaseHTTPRequestHandler
import json
import os

data = {'code':'200','result': '开始爬取'}
host = ('192.168.1.172', 8090)

class Resquest(BaseHTTPRequestHandler):
    def do_GET(self):
        os.system('/root/.pyenv/bin/pyenv local 3.7.3')
        os.system('cd /var/html/spider-taobao/')
        os.system('nohup /root/.pyenv/shims/python  -u /var/html/spider-taobao/main.py > test.log 2>&1 &')
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()
        self.wfile.write(json.dumps(data).encode())

    def do_POST(self):
        line = ''

        with open('test.log', 'r+') as f:
            line = f.read()
        result = {'code':'200','result': line}
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()
        self.wfile.write(json.dumps(result).encode())

if __name__ == '__main__':
    server = HTTPServer(host, Resquest)
    server.serve_forever()
