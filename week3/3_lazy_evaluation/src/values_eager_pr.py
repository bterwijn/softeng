from helpers import pr

n = 5
values = [pr('create:', i) for i in range(5)]
print('list is created')
for i in values:
    pr('use:', i)
