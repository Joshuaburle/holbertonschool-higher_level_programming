#!/usr/bin/python3
"""Simple API using Python's http.server module"""

from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse
import json


class SimpleAPIHandler(BaseHTTPRequestHandler):
    def _send_text(self, status_code: int, message: str) -> None:
        body = message.encode("utf-8")
        self.send_response(status_code)
        self.send_header("Content-Type", "text/plain")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def _send_json(self, status_code: int, payload: dict) -> None:
        body = json.dumps(payload).encode("utf-8")
        self.send_response(status_code)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def do_GET(self):
        # IMPORTANT: ignore query string (?x=1)
        path = urlparse(self.path).path

        if path == "/":
            self._send_text(200, "Hello, this is a simple API!")
        elif path == "/status":
            self._send_text(200, "OK")
        elif path == "/data":
            self._send_json(200, {"name": "John", "age": 30, "city": "New York"})
        elif path == "/info":
            self._send_json(200, {"version": "1.0", "description": "A simple API built with http.server"})
        else:
            # Expected by spec: 404 + message "Endpoint not found"
            self._send_text(404, "Endpoint not found")


def run():
    server = HTTPServer(("0.0.0.0", 8000), SimpleAPIHandler)
    server.serve_forever()


if __name__ == "__main__":
    run()
