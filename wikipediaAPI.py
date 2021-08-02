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

def getAndAppendItems(FinalList, category):
    URL = "https://en.wikipedia.org/w/api.php"

    PARAMS = {
        "action": "query",
        "format": "json",
        "list": "categorymembers",
        "cmtitle": category
    }

    R = S.get(url=URL, params=PARAMS)
    DATA = R.json()
    while True:
        for item in DATA["query"]["categorymembers"]:
            if "Category:" in item["title"]:
                getAndAppendItems(FinalList, item["title"])
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
    getAndAppendItems(FinalList, "Category:Cats")

    with open('./json/outputCat.json', "w") as fl:
        json.dump(FinalList, fl)



