from flask import Flask
from flask_cors import CORS
import filestream as fs
from service.conf import CONFIG
from service.database_connector import DatabaseConnector

DATABASE_CONFIG = CONFIG["database"]
SERVER_CONFIG = CONFIG["server"]

dbConnector = DatabaseConnector(    DATABASE_CONFIG["user"],
                                    DATABASE_CONFIG["password"],
                                    DATABASE_CONFIG["host"],
                                    DATABASE_CONFIG["port"],
                                    DATABASE_CONFIG["database"]
                                )
db_ok = dbConnector.connect()

origin = SERVER_CONFIG["webapp_address"]

app = Flask(__name__)
CORS(app, resources={r"/comics": { "origins": origin } })

@app.route("/")
def home():
    return "Comics Finder REST Service"

@app.route("/comics")
def list_comics():
    if db_ok:
        data = dbConnector.query("SELECT * FROM comic_simple")
        return { "comics": data }
