__author__ = 'Eric'
b=0
for a in range(10,300):
    b=(1000*a-500000)/(a-1000)
    if int(b) == b:
        break
print(a,b)