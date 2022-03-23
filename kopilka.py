#1
i = int(input('Сколько хотите накопить: '))
s = 0
while True:
    a = int(input('Взнос: '))
    s += a
    if s >= i:
        print('Поздравляю! Вы накопили: ', s)
        break


