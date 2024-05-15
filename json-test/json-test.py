import json

#x = '{ "key2":"value2", "key3":"value3", "key4":"value4", "key5":"value5" }'
x = '{ "key1":"value1", "key2":"value2", "key3":"value3", "key4":"value4", "key5":"value5" }'

jsonx = json.loads(x)
number = len(jsonx)
print(json.dumps(jsonx, indent=3))
#print(number)
