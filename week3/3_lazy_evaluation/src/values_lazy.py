n = 5
values = (i for i in range(5))
print(values)  # <generator object ...>
print(list(values))  # [0, 1, 2, 3, 4]
print(list(values))  # []   generator is used up
print(list(values))  # []   generator is used up
