import json

if __name__ == "__main__":
    finalList = []
    with open("./json/outputCat.json") as fl:
        jsnFl = json.load(fl)
        for entry in jsnFl:
            newEntry = {}
            entry = next(iter(entry.values()))
            #newEntry["title"] = entry["title"]
            newEntry["fullurl"] = entry["fullurl"]
            newEntry["displaytitle"] = entry["displaytitle"]
            finalList.append(newEntry)

    with open("./json/outputCatSmall.json", "w") as fl:
        json.dump(finalList, fl)
