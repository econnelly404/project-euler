__author__ = 'Eric'

import math
def prime(n):
    if n % 2 == 0 and n > 2:
        return False
    return all(n % i for i in range(3, int(math.sqrt(n)) + 1, 2))

largestFactor = 0
for num in range(1, int(600851475143/2)+1, 2):
    if 600851475143 % num == 0:
        if prime(num):
            largestFactor = num
print(largestFactor)