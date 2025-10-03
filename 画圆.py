import math

x=input("圆心x轴坐标：")
y=input("圆心y轴坐标：")
r=input("圆的半径：")
x=int(x)
y=int(y)
r=int(r)
for i in range(0, r):
    x1 = x + i
    y1 = y + math.sqrt(r**2 - i**2)
    y_int = round(y1)
    print("点坐标：({}, {})".format(x1, y_int))