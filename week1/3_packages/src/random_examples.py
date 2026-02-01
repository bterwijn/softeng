import random
random.seed(0)  # use same random numbers each run

a, b = 0, 4
print( random.randint(a, b)   ) # 3         random int from a through b
print( random.randrange(a, b) ) # 3         random int from a to b
print( random.random()        ) # 0.041...  random float from 0.0 to 1.0
print( random.uniform(a, b)   ) # 3.861...  random float from a to b

mylist = [1, 2, 3]
print( random.choice(mylist) )       # 2       choose 1 random value from list
print( random.choices(mylist, k=2) ) # [2, 3]  choose k values with repetition
print( random.sample(mylist, k=2) )  # [2, 3]  choose k values without repetition
print( random.shuffle(mylist) )      # None    gives mylist a random order

print( random.gauss(mu=0.0, sigma=1.0)) # -0.813... random float from
                                        #           normal distribution
