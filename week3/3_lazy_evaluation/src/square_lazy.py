n = 5

values = (i for i in range(n))
values = (i**2 for i in values)
for i in values:
    print('result:', i)
