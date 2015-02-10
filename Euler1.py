__author__ = 'Eric'
threes = 0
fives = 0
sum = 0
for num in range(1000):
    if num % 3 == 0:
        threes = threes + num
    elif num % 5 == 0:
        fives = fives + num
print(threes + fives)