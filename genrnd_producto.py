from itertools import combinations
import random
import math

num_rand = []

def genrnd(a, b):
    for i in range(50):
        num_rand.append(random.uniform(a,b))
        
def comb_prod(c):
    temp = combinations(c, 2)
    for i in list(temp):
        print(math.prod(i))
        
genrnd(100, 200)
print(num_rand)

comb_prod(num_rand)