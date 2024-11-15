from http.server import HTTPServer, BaseHTTPRequestHandler
content = """
<html>
    <body bgcolor="lavender">
        <h1 align="center"><u><i>DEVICE CONFIGURATION</u></i></h1>
        <h2 align="center">Rhudhra phriyamvadha</h2>
        <h3 align="center">Reg.no:24900189</h3>
        <ul type="star">
            <li>Device name: phriyamvadha19</li>
            <li>Processor: 13th Gen Intel(R) Core(TM) i5-1334U   1.30 GHz</li>
            <li>Installed RAM: 8.00 GB (7.69 GB usable)</li>  
            <li>Device ID: 45F38CCB-F454-419E-9FC6-E084F180109B</li> 
            <li>Product ID: 00356-24756-97694-AAOEM</li>
            <li>System type: 64-bit operating system, x64-based processor</li>
            <li>Pen and touch: No pen or touch input is available for this display</li>  
        </ul> 
    </body>
</html>


"""
class myhandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print("request received")
        self.send_response(200)
        self.send_header('content-type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(content.encode())
server_address = ('',8000)
httpd = HTTPServer(server_address,myhandler)
print("my webserver is running...")
httpd.serve_forever()
