from flask import Flask
from flask_cors import CORS
import filestream as fs
import yaml

conf_filepath = "conf.yml"

f = open(conf_filepath, "r")
conf_data = yaml.full_load(f)
f.close()

COMICS_DATA_PATH = conf_data["data_path"]

origin = "http://localhost:" + str(conf_data["webapp_port"])

app = Flask(__name__)
CORS(app, resources={r"/comics": {"origins": origin } })

@app.route("/")
def home():
    return "Comics Finder REST Service"

@app.route("/comics")
def list_comics():
    comics_data = fs.read_data_as_json(COMICS_DATA_PATH)
    return comics_data

if __name__ == "__main__":
    app.run()
