#1

a = [1, 2, 3, 4,]
a.append('salam')
a.append(True)

#2

names = ['JACK', 'JIMMY', 'JACKSON', 'JHON', 'JACKSON', 'JHON', 'JIMMY', 'JACKSON', 'JHON','JACK', 'JIMMY', 'JACK', 
'JACKSON', 'JHON', 'JACKSON', 'JHON','JACK', 'JIMMY', 'JACK', 'JACKSON', 'JHON',]

name = names.count('JACK')
print(name)

#3

del names[0:11:2]
print(names)
