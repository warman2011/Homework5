with open ('lesson1.txt', 'w') as f:
    while True:
        text = input('Какой текст записать: ')
        f.writelines(text+'\n')
        if text == '':
            break