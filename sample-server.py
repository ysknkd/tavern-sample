import http.server
import socketserver
from http import HTTPStatus


class SampleHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        print("header['Sample-Token'] =", self.headers['Sample-Token'])
        self.send_response(HTTPStatus.OK)
        self.end_headers()
        self.wfile.write(b'Hello World')


PORT = 3000
with socketserver.TCPServer(("", PORT), SampleHandler) as httpd:
    print("serving at port =", PORT)
    httpd.serve_forever()
