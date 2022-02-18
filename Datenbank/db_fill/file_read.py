import json

def json_read(path):
    with open(path, 'r', encoding="utf-8") as file:
        obj = json.load(file)
    return shorten(obj)

def shorten(obj):
    kanjis = obj['kanjis']
    list = []
    for item in kanjis:
        k = kanjis[item]
        if len(k['kun_readings']) > 0 and len(k['on_readings']) > 0 and k['jlpt'] != None and len(k['meanings']) > 0:
            list.append(k)
    return list