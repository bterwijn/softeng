def add(a=100, b=200):
    return a + b

print('add(1, 2):', add(1, 2) )  # calls add(  1,   2)
print('add(1):',    add(1)    )  # calls add(  1, 200)
print('add():',     add()     )  # calls add(100, 200)
