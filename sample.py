import json

#jsobj = json.load(open('sample.json'))
jsdata = open('sample.json','r')
jsobj = json.load(jsdata)

print(jsobj['people'])