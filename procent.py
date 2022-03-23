#1
a = int(input())
o = 0
e = 0
p = 0
for i in range(1, a + 1):
    if i % 2 == 0:
        e += 1
print(e)