url=input()
for i in range(len(url)):
    a=ord(url[i])
    if 100<=a<=122 or 68<=a<=90:
        a1=chr(a-3)
    elif 97<=a<=99 or 65<=a<=67:
        a1=chr(a+23)
    else:
        a1=chr(a)
    print(a1,end='')