#1
while True:
    for a in range(1, 1001):
        print(a)
    if a == 1000:
        break

#2
while True:
    i = int(input('Введите: '))
    if i < 100:
        print(i)
    else:
        print('Вы ввели число больше 100')