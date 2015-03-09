# a truly minimal HTTP proxy

import SocketServer
import SimpleHTTPServer
try:
    from urllib.request import Request, urlopen  # Python 3
except:
    from urllib2 import Request, urlopen  # Python 2

PORT = 8080

class Proxy(SimpleHTTPServer.SimpleHTTPRequestHandler):
    def do_GET(self):
        if(self.path.startswith("/proxy/")):
            req = Request("http://"+self.path[7:])
            req.add_header("Accept", "application/json")
            self.copyfile(urlopen(req), self.wfile)
        else:
            SimpleHTTPServer.SimpleHTTPRequestHandler.do_GET(self)

httpd = SocketServer.ForkingTCPServer(('', PORT), Proxy)
print "serving at port", PORT
httpd.serve_forever()
