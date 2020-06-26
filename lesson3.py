summ = 0
with open ('lesson3.txt', 'r') as f:
    lines = [i for i in f.readlines()]
    f.seek(0)
    for a in range(1, len(lines)+1):
        line = f.readline().split()
        if int(line[1]) < 20000:
            print('Оклад менее 20000 у:', line[0])
    f.seek(0)
    for a in range(1, len(lines)+1):
        x, y = f.readline().split()
        summ += int(y)
    print('Средняя зарплата:', '{:.2f}'.format(summ/(a-1)))
