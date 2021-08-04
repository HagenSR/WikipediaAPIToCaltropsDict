import sys

import requests
import json

def requestPageInformationThenAppend(FinalList, item):
    URL = "https://en.wikipedia.org/w/api.php"

    PARAMS = {
        "action": "query",
        "format": "json",
        "pageids": item["pageid"],
        "prop": "info",
        "inprop": "url|displaytitle"
    }

    R = S.get(url=URL, params=PARAMS)
    DATA = R.json()
    FinalList.append(DATA["query"]["pages"])

def getAndAppendItems(FinalList, category, depth):
    URL = "https://en.wikipedia.org/w/api.php"

    PARAMS = {
        "action": "query",
        "format": "json",
        "list": "categorymembers",
        "cmtitle": category
    }

    R = S.get(url=URL, params=PARAMS)
    DATA = R.json()
    next_depth = depth + 1
    while True:
        for item in DATA["query"]["categorymembers"]:
            if "Category:" in item["title"] and depth < 6:
                getAndAppendItems(FinalList, item["title"], next_depth)
            elif "Category:" in item["title"]:
                continue
            else:
                requestPageInformationThenAppend(FinalList, item)
        if "continue" not in DATA:
            break
        PARAMS["cmcontinue"] = DATA["continue"]["cmcontinue"]
        R = S.get(url=URL, params=PARAMS)
        DATA = R.json()

if __name__ == "__main__":
    FinalList = []
    S = requests.Session()
    depth = 1
    getAndAppendItems(FinalList, "Category:Mythology", depth)

    with open('./json/outputMythology.json', "w") as fl:
        json.dump(FinalList, fl)



