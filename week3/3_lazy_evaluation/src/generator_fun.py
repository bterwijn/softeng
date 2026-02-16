def generator_function(n):
    i = 0
    while i < n:
        yield i
        i += 1

n = 5
gen = generator_function(n)
for i in gen:
    print(i, end=' ')  # 0 1 2 3 4