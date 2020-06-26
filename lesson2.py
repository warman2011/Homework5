with open ('lesson2.txt', 'r') as f:
    line = [i for i in f.readlines()]
    print('Количество строк в файле:', len(line))
    f.seek(0)
    for a in range(1, len(line)+1):
        line = f.readline().split()
        print('Количество слов в строке №', str(a), ':', len(line))