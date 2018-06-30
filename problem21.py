from math import sqrt
from time import time
def factor_sum(n):
    return sum([k for i in range(1, int(sqrt(n))+1) if not n%i for k in (i, n//i)])-n
def is_amicable(n):
    a = factor_sum(n)
    if a==n:
        return False
    return n==factor_sum(a)
t0 = time()
top = 10 ** 4
print(sum([i for i in range(top) if is_amicable(i)]), time()-t0)