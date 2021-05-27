import web
import filestream as fs

COMICS_DATA_PATH = "comics_data.json"

urls = (
    '/comics', 'list_comics',
    '/comics/(.*)', 'get_comic'
)

app = web.application(urls, globals())

class list_comics:
    def GET(self):
        comics_data = fs.read_data_as_json(COMICS_DATA_PATH)
        return comics_data["comics"]

class get_comic:
    def GET(self, user):
        comics_data = fs.read_data_as_json(COMICS_DATA_PATH)
        for child in comics_data["comics"]:
            if child["id"] == int(user):
                return child

if __name__ == "__main__":
    app.run()
