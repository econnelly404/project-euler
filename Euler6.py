__author__ = 'Eric'
sum = 0
squares = 0
for i in range(1,101):
    sum = sum + i
    squares = squares + i**2
print(sum**2 - squares)