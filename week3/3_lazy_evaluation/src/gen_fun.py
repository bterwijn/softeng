
def generator_function(n):
    for i in range(n):
        yield i

n = 5
gen = generator_function(n)
print(gen)  # <generator_function at 0x7...>
print(list(gen))  # [0, 1, 2, 3, 4]
print(list(gen))  # []   generator is used up
gen = generator_function(n)
print(list(gen))  # [0, 1, 2, 3, 4] new vales