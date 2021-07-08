import json
def getUrls():
    return json.load(open('result1.json',))

print(getUrls()[85])