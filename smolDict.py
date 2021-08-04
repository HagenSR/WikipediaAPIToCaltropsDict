import json

if __name__ == "__main__":
    finalDict = {}
    with open("./json/outputCat.json") as fl:
        jsnFl = json.load(fl)
        for entry in jsnFl:
            entry = next(iter(entry.values()))
            finalDict[entry["fullurl"]] = entry["displaytitle"]

    with open("./json/outputCatSmall.json", "w") as fl:
        json.dump(finalDict, fl)
