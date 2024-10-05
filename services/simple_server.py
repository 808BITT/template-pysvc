from services import Service
import http.server

class SimpleServer(Service):
    '''
    A simple HTTP server that serves files from the current directory
    
    Args:
        stop (Event): An instance of threading.Event to stop the server
    '''

    def __init__(self, stop):
        super().__init__(stop, name="SimpleServer", daemon=False)

    def run(self):
        simple_server = http.server.HTTPServer(('localhost', 8000), http.server.SimpleHTTPRequestHandler)
        simple_server.timeout = 1
        
        print("Start 2")
        while not self.stop.is_set():
            simple_server.handle_request()
        simple_server.server_close()
        print("End 2")