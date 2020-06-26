with open('lesson4.txt', 'r') as f:
    summ = [i for i in f.readlines()]
    f.seek(0)
    for i in range(1, len(summ)+1):
        list = f.readline().split('-')
        if list[0] == 'One':
            list[0] = 'Один'
        elif list[0] == 'Two':
            list[0] = 'Два'
        elif list[0] == 'Three':
            list[0] = 'Три'
        elif list[0] == 'Four':
            list[0] = 'Четыре'
        print(list)
        f_obj = open('lesson4.1.txt', 'a')
        f_obj.writelines('-'.join(list))
