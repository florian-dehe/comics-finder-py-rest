from service_readonly import COMICS_DATA_PATH
import comic
import filestream as fs

# This program asks for a comic to add to the data set

COMICS_DATA_PATH = "comics_data.json"

def ask_new_comic():
    print("==========================")
    print("Create a new comic entry :")
    
    print("Collection : ", end="")
    collection = input()

    print("Serie : ", end="")
    serie = input()

    print("Volume : ", end="")
    volume = input()

    print("Title : ", end="")
    title = input()

    print("Authors : ", end="")
    authors = input()

    print("Cover (URL) : ", end="")
    cover = input()

    print("Comment : ", end="")
    comment = input()
    print("==========================")

    return comic.Comic(collection, serie, volume, title, authors, cover, comment)

def main():
    obj = ask_new_comic()

    data = fs.read_data_as_json(COMICS_DATA_PATH)
    data["comics"].append(obj.save_to_json(len(data["comics"])+1))

    fs.write_data_as_json(COMICS_DATA_PATH, data)

if __name__ == "__main__":
    main()