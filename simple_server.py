import http.server
import socketserver
import sys

PORT = 9000

handler = http.server.SimpleHTTPRequestHandler

print(f"Starting server at port {PORT}...")
print(f"Visit http://localhost:{PORT}/student_info.html to view student information page")

try:
    with socketserver.TCPServer(("localhost", PORT), handler) as httpd:
        print(f"Server running...")
        httpd.serve_forever()
except KeyboardInterrupt:
    print("\nServer stopped by user")
except Exception as e:
    print(f"Error occurred: {e}")
    sys.exit(1)