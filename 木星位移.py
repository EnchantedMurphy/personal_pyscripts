sum = 0
for x in range(1,121):
    y = -x**2/100000 + x*0.00007 +0.1999
    sum = sum + y
print(sum)