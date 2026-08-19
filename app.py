from http.server import BaseHTTPRequestHandler, HTTPServer
import json


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        response = {
            "status": "ok",
            "version": "2.0"
        }

        body = json.dumps(response).encode()

        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)


def handler(event):
    return {
        "status": "ok",
        "version": "1.0"
    }


if __name__ == "__main__":
    server = HTTPServer(("0.0.0.0", 80), Handler)

    print("Server running on port 80")

    server.serve_forever()
