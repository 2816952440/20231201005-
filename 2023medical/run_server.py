import http.server
import socketserver
import sys

PORT = 8002

handler = http.server.SimpleHTTPRequestHandler

print(f"启动服务器在端口 {PORT}...")
print(f"访问 http://localhost:{PORT}/student_info.html 查看学生信息页面")

try:
    with socketserver.TCPServer(("", PORT), handler) as httpd:
        print(f"服务器运行中...")
        httpd.serve_forever()
except KeyboardInterrupt:
    print("\n服务器已停止")
except Exception as e:
    print(f"发生错误: {e}")
    sys.exit(1)