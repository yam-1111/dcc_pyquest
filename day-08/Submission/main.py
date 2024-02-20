import json

files = {
    "csv" : "/home/vee/Personal/15-Days-of-Python/day-08/example1.csv",
    "json" : "/home/vee/Personal/15-Days-of-Python/day-08/example2.json"
}

for key,value in files.items():
    if key == "csv":
        file = "\n".join(list(x.split(',')[0] for x in (open(value).readlines())[1:-1]))
        print(file)
    if key == "json":
       file = json.load(open(value, 'r'))
       print(json.dumps(file, indent=2))