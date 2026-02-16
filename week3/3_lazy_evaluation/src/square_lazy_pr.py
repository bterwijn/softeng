from helpers import pr 

n = 5

values = (pr('init:', i) for i in range(n))
values = (pr('square:',i**2) for i in values)
for i in values:
    print('result:', i)
