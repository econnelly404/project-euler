__author__ = 'Eric'
def tri(n):
    if n == 1:
        return 1
    else:
        return tri(n-1) + n

done = False
x = 1

while not done:
    count = 0
    for i in range(1, tri(x)+1):
        if tri(x) % i == 0:
            count += count
        if count > 500:
            print(tri(x))
            break
    if count > 500:
        break