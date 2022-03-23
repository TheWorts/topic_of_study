0
b = '''Ваши действие:
1. Добавить новый город
2. Отобразить список городов
3. Заменить город
4. Удалить город
5. Выход'''
city = []
while  True:
    print()
    print(b)
    a = input('Введите ваши действия: ')
    if a == '1':
        a = input('Добавить новый город: ')
        if a in city :
            print('Такой город уже есть')
        else:
            city.append(a)
    if a == '2':
        print(city)
    if a == '3':
        s = input('заменить на город: ')
        print(city)
        c = input('какой город заменить?: ')
        r = city.remove(c)
        city.append(s)
    if a == '4':
        z = input('Какой город удалить: ')
        city.remove(z)
    if a == '5':
        break

