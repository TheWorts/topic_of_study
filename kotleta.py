k = int(input('сковорода вмещает: '))
m = int(input('сколько котлет: '))
n = int(input('сколько минут нужно жарить? : '))
if n <= k :
    v = 2 * m
elif n * 2 % k == 0:
    v = m * (n * 2 // k)
else:
    v = m * (1 + (n * 2 // k))
print(v)