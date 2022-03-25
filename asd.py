from random import randint
from os import system
for i in range(5):
    r = randint(1, 10)
    system(f'touch/home/erbol/Рабочий стол/github/{r}.txt')
