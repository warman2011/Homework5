slov = {}
a = 0
with open ('lesson6.txt', 'r') as f:
    summ = [i for i in f.readlines()]
    f.seek(0)
    for i in range(1,len(summ)+1):
        list = f.readline().split(' ')
        a = 0
        for i in range(0, len(list)):
            b = list[i].split('(')
            if b[0].isdigit() > 0:
                a += int(b[0])
        slov[list[0]] = a
    print(slov)