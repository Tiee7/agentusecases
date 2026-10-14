import threading
import unittest
from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.error import HTTPError
from agentwatch.crawler import fetch

class RedirectTests(unittest.TestCase):
    def test_redirect_does_not_fetch_unreviewed_path(self):
        visited=[]
        class Handler(BaseHTTPRequestHandler):
            def do_GET(self):
                visited.append(self.path)
                self.send_response(302)
                self.send_header('Location','/api/forbidden')
                self.end_headers()
            def log_message(self,*args):
                pass
        server=HTTPServer(('127.0.0.1',0),Handler)
        thread=threading.Thread(target=server.serve_forever,daemon=True)
        thread.start()
        try:
            with self.assertRaises(HTTPError) as error:
                fetch(f'http://127.0.0.1:{server.server_port}/case')
            self.assertEqual(error.exception.code,302)
            self.assertEqual(visited,['/case'])
        finally:
            server.shutdown()
            server.server_close()
            thread.join()
