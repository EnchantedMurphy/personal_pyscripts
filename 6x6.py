x = [5]
y = [18]
for a in range(1,6):
    x.append(x[0] + a * 36)
    y.append(y[0] + a * 36)
for i in range(5, -1, -1):
    print(x[i])
print('  ',end=' ')
for i in range(0,6):
    print(y[i],end=' ')
