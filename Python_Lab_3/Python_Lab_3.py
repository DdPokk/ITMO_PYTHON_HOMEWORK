from statistics import mean
from statistics import median
from statistics import stdev
from math import fsum
from random import randint

x = [randint(0, 100) for i in range(10)]
print(x)

print(fsum(x))
print(mean(x))
print(median(x))
print(stdev(x))

print(randint(1,100))