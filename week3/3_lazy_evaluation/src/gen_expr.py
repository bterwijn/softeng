
def generator_expression(n):
    return (i for i in range(n))


n = 5
gen = generator_expression(n)
print(gen) # <generator_expression at 0x7...>
print(list(gen))  # [0, 1, 2, 3, 4]
print(list(gen))  # []   generator is used up
gen = generator_expression(n)
print(list(gen))  # [0, 1, 2, 3, 4] new values