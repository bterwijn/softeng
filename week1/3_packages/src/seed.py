import random

for i in range(10):
    random.seed(0)  # resets the random seed in each iteration of the loop, BAD!
    print(random.randrange(10), end=' ')  # 6 6 6 6 6 6 6 6 6 6
