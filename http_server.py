from http.server import HTTPServer, BaseHTTPRequestHandler
import urllib.parse as up

test = {}
test["1"] = "doc_2018"

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        query = up.parse_qs(self.path[2:])
        #print(query["query"])
        self.wfile.write(bytes(test[query["query"][0]],'utf-8'))


httpd = HTTPServer(('localhost', 8000), SimpleHTTPRequestHandler)
httpd.serve_forever()