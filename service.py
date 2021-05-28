from flask import Flask
from flask_cors import CORS
import filestream as fs

COMICS_DATA_PATH = "comics_data.json"

origin = "http://localhost:3000"

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
