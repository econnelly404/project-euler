__author__ = 'Eric'
import math
def prime(n):
    if n % 2 == 0 and n > 2:
        return False
    return all(n % i for i in range(3, int(math.sqrt(n)) + 1, 2))
count =0
number = 2
while count != 6:
    if prime(number):
        count += 1
        number += number
    else:
        number += number

print(number)
