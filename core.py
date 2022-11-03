from http.server import BaseHTTPRequestHandler, HTTPServer
import logging
from urllib.parse import unquote
import tuxedo_keyboard




class S(BaseHTTPRequestHandler):

    def do_GET(self):
        buffer = (unquote(self.path)[:-1]).lstrip("/").lstrip("[")
        buffer = buffer.split(",")
        keyboard.setcolor(keyboard.rgb_to_hex((int(buffer[0]),int(buffer[1]),int(buffer[2]))))



def run(server_class=HTTPServer, handler_class=S, port=6670):
    logging.basicConfig(level=logging.INFO)
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    logging.info('Starting daemon\n')
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()
    logging.info('Stopping daemon\n')

if __name__ == '__main__':
    from sys import argv

    if len(argv) == 2:
        run(port=int(argv[1]))
    else:
        run()