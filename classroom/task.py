#1 and 4
dict1 = {'drinks': ['coca-cola', 'sprite', 'fanta']}

dict1.update(besh_barmak = 130, borsh = 122, lagman = 120)

del dict1['borsh']

dict1['besh_barmak'] = 135

print(dict1)

#2

dict2 = {  
              }
for i in range(3):
    q = input('Введите ваше имя: ')
    q2 = input('Введите ваш пароль: ')
    dict2[q] = q2
print(dict2)

#3

dict3 = {'erlan': 'programmer', 'vasia': 'cto'}

for name, prof in dict3.items():
    print('Здраствуйте: ',  name, 'Профессия: ', prof)


