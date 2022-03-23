#1
number_dict = {'first': 1, 'second': 2, 'third': 3}
new_dict = {key: value **3 for key, value in number_dict.items()}
print(new_dict)

#2
number_list = [6, 43, 0, -2, 11, -55, -12, 3, 345]
number_dict1 = {number : number ** 2 for number in number_list}
number_dict2 = {number : 'positive' if number > 0 else 'negative' if number < 0 else 'zero' for number in number_list}
print(number_dict1)

#SET COMPREHESION
number_list2 = [6, 43, 0, -2, 11, -55, -12, 3, 345]
number_set = {number ** 2 for number in number_list2}
print(number_set)
letter_set = {letter.upper() for letter in 'hello'}
print(letter_set)