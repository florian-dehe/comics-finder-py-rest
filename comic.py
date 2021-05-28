
#Comic obj used to describe a comic and save it as JSON.
class Comic:
    def __init__(self, collection : str, serie : str, volume: str, title: str, authors : str, cover : str, comment :str):
        self.collection = collection
        self.serie = serie
        self.volume = volume
        self.title = title
        self.authors = authors
        self.cover = cover
        self.comment = comment
    
    def save_to_json(self, id : int):
        obj_data = {    "id": id,
                        "collection": self.collection,
                        "serie": self.serie,
                        "volume": self.volume,
                        "title": self.title,
                        "authors": self.authors,
                        "cover": self.cover,
                        "comment": self.comment
                        }
        return obj_data