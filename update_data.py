import comic
import filestream as fs
import yaml

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
    f = open("conf.yml")
    conf_data = yaml.full_load(f)
    f.close()

    comics_data_path = conf_data["data_path"];

    obj = ask_new_comic()

    json_data = fs.read_data_as_json(comics_data_path)
    json_data["comics"].append(obj.save_to_json(len(json_data["comics"])+1))

    fs.write_data_as_json(comics_data_path, json_data)

if __name__ == "__main__":
    main()
