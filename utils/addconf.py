import json

configpath = "./../config/config.json"

def add_conf(name,url):

    f = open(configpath)
    data = json.load(f)["data"]

    # check if name or url already exist
    for i in data:
        for j in i:
            print()
    f.close()

    # write the latest content to the json file
    # f = open(homepath, "w")
    # json_object = json.dumps(data, indent=4)
    # f.write(json_object)
    # f.close()

add_conf("","")