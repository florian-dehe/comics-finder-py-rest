from gevent.pywsgi import WSGIServer
from service.service import app
from service.conf import CONFIG

SERVER_CONFIG = CONFIG["server"]

def launch_server():
    port = SERVER_CONFIG["server_port"]
    http_server = WSGIServer(('',  port), app)
    try:
        print("Server started on http://localhost:" + str(port) + "/.")
        http_server.serve_forever()
    except KeyboardInterrupt:
        print("Server stopped.")
