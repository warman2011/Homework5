import json
average = 0
a = 0
ap = {}
db = {}
x = []
with open ('lesson7.txt', 'r') as f:
    lines = [i for i in f.readlines()]
    f.seek(0)
    for i in range(1, 6):
        line = f.readline().split()
        if int(line[2]) > int(line[3]):
            average = int(line[2]) - int(line[3])
            db[line[0]] = average
            a += average
        elif int(line[2]) < int(line[3]):
            average = int(line[2]) - int(line[3])
            db[line[0]] = average
    ap['average_profit'] = a
    x.append(db)
    x.append(ap)
    print(x)
with open('lesson7.json', 'w') as f_obj:
    json.dump(x, f_obj)
