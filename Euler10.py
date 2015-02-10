__author__ = 'Eric'
import math
def prime(n):
    if n % 2 == 0 and n > 2:
        return False
    return all(n % i for i in range(3, int(math.sqrt(n)) + 1, 2))
sum = 0
for i in range(2,2000000):
    if prime(i):
        sum = sum +i
print(sum)