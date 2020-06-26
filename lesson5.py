with open('lesson5.txt', 'w') as f:
    f.writelines('34 34 42 234 53 23 345 4353 23 2')
with open('lesson5.txt', 'r') as f:
    print(sum(map(int, f.read().split())))