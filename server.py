from gevent.pywsgi import WSGIServer
from service import app
import yaml

conf_filepath = "conf.yml"

f = open(conf_filepath, "r")
conf_data = yaml.full_load(f)
f.close()

port = conf_data["server_port"]
http_server = WSGIServer(('',  port), app)
try:
    print("Server started on http://localhost:" + str(port) + "/.")
    http_server.serve_forever()
except KeyboardInterrupt:
    print("Server stopped.")
