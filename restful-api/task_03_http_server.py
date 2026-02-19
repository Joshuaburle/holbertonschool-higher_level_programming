#!/usr/bin/python3
"""
Simple API using Python's http.server module
Endpoints:
- /            -> plain text welcome message
- /status      -> plain text "OK"
- /data        -> JSON sample data
- /info        -> JSON info (optional but mentioned in expected output)
- anything else -> 404 JSON error
"""

from http.server import BaseHTTPRequestHandler, HTTPServer
import json


class SimpleAPIHandler(BaseHTTPRequestHandler):
    def _send_text(self, status_code: int, message: str) -> None:
        """Send a plain text response."""
        self.send_response(status_code)
        self.send_header("Content-Type", "text/plain; charset=utf-8")
        self.end_headers()
        self.wfile.write(message.encode("utf-8"))

    def _send_json(self, status_code: int, payload: dict) -> None:
        """Send a JSON response."""
        body = json.dumps(payload).encode("utf-8")
        self.send_response(status_code)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def do_GET(self):
        """Handle GET requests."""
        if self.path == "/":
            self._send_text(200, "Hello, this is a simple API!")
        elif self.path == "/status":
            self._send_text(200, "OK")
        elif self.path == "/data":
            self._send_json(200, {"name": "John", "age": 30, "city": "New York"})
        elif self.path == "/info":
            self._send_json(200, {"version": "1.0", "description": "A simple API built with http.server"})
        else:
            self._send_json(404, {"error": "Endpoint not found"})

    def do_POST(self):
        """Optional: basic POST handler to show method handling."""
        self._send_json(405, {"error": "Method not allowed"})


def run_server(host: str = "0.0.0.0", port: int = 8000) -> None:
    server = HTTPServer((host, port), SimpleAPIHandler)
    print(f"Server running on http://localhost:{port}")
    server.serve_forever()


if __name__ == "__main__":
    run_server()
