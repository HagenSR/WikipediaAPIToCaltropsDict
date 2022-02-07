import json

def writeOnlyLinksAndDesc():
    finalDict = {}
    with open("./json/outputComputing.json") as fl:
        jsnFl = json.load(fl)
        for entry in jsnFl:
            entry = next(iter(entry.values()))
            finalDict[entry["fullurl"]] = entry["displaytitle"]

    with open("./json/outputComputerSmall.json", "w") as fl:
        json.dump(finalDict, fl)

def pickEveryOther():
    finalDict = {}
    with open("./json/outputMythSmall.json") as fl:
        jsn_fl = json.load(fl)
        flip = False
        for entry in jsn_fl:
            if flip:
                finalDict[entry] = jsn_fl[entry]
            flip = not flip

    with open("./json/outputMythSmall.json", "w") as fl:
        json.dump(finalDict, fl)

def list_to_dict():
    jsn_list = []
    jsn_rtn = {}
    with open("json\\final_results.json") as fl:
        jsn_list = json.load(fl)
    for entry in jsn_list:
        jsn_rtn[entry["wiki_url"]] = "Desc Needed"
    with open("json\\final_results_dict.json", 'w') as fl:
        json.dump(jsn_rtn, fl)

def mergeDict():
    finalDict = {}
    with open("json\\final_results_dict.json") as fl:
        jsn_fl = json.load(fl)
        with open("json\\unusual.json") as fl2:
            jsn_fl_2 = json.load(fl2)
            print(f"Original_Length: {len(jsn_fl_2)}")
            finalDict = {**jsn_fl_2, **jsn_fl}
            with open("json\\unusual.json", "w") as fl:
                print(f"Final length: {len(finalDict)}")
                json.dump(finalDict, fl)

if __name__ == "__main__":
    mergeDict()
