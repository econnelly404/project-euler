product = ""
half1 = ""
half2 = ""
pal = 1
for i in range(100,1000):
    for j in range(100,1000):
        product = str(i*j)
        if len(product) == 5:
            half1 = product[0:2]
            half2 = product[4:2:-1]
            if half1 == half2 and int(product)>pal:
                pal = int(product)
        if len(product) == 6:
            half1 = product[0:3]
            half2 = product[5:2:-1]
            if half1 == half2 and int(product)>pal:
                pal = int(product)
print(pal)
print(half1)
print(half2)