
from http.server import BaseHTTPRequestHandler, HTTPServer
import json
from datetime import datetime

alerts = []

class RequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        if self.path == "/alerts":
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps(alerts).encode())

        else:
            self.send_response(200)
            self.end_headers()
            self.wfile.write("AI Surveillance Backend Running")

    def do_POST(self):
        if self.path == "/alert":
            content_length = int(self.headers["Content-Length"])
            body = self.rfile.read(content_length)
            data = json.loads(body)

            alert = {
                "type": data.get("type", "unknown"),
                "confidence": data.get("confidence", 0),
                "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            }

            alerts.append(alert)

            print("🚨 ALERT RECEIVED:", alert)

            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(b'{"status":"success"}')
