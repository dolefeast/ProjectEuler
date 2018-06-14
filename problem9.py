from math import sqrt
from time import time
class Breaker(Exception):
    pass
p=1000
t0=time()
try:
    for a in range(1,p//2):
        for c in range(1,p-2*a):
            b=p-a-c
            if a*b==p**2//2-p*c: #proven mathematically
                print(a*b*c, time()-t0)
                raise Breaker
except Breaker:
    pass