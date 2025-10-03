x = [5]
y = [18]
for a in range(6):
    x.append(x[0] + a * 36)
    y.append(y[0] + a * 36)
print(x[6])
print(x[5])
print(x[4])
print(x[3])
print(x[2])
print(x[1])
print('  ',y[1],y[2],y[3],y[4],y[5],y[6])