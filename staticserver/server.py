import http.server
import base64

USERNAME = 'pusheen'
PASSWORD = 'stormy'
BASIC_AUTH_STRING = f"{USERNAME}:{PASSWORD}".encode('utf-8')
BASIC_AUTH_BASE64 = base64.b64encode(BASIC_AUTH_STRING).decode('utf-8')

class AuthHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_HEAD(self):
        self.send_response(401)
        self.send_header('WWW-Authenticate', 'Basic realm=\"Authorization required\"')
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(b'Authorization required')

    def authorize(self):
        if self.headers.get('Authorization') is None:
            self.do_HEAD()
            self.wfile.write(b'Authorization header missing')
            return False
        elif self.headers.get('Authorization') != 'Basic ' + BASIC_AUTH_BASE64:
            self.do_HEAD()
            self.wfile.write(b'Authorization credentials incorrect')
            return False
        return True

    def do_GET(self):
        if not self.authorize():
            return
        super().do_GET()

    def do_POST(self):
        if not self.authorize():
            return
        super().do_POST()

if __name__ == '__main__':
    http.server.test(HandlerClass=AuthHTTPRequestHandler)
