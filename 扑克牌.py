import random


unowned = [3,3,3,4,4,4,4,4,5,5,5,5,5,6,6,6,6,6,6,6,6,7,7,7,7,7,7,7,8,8,8,8,8,8,9,9,9,9,9,9,9,9,10,10,10,10,10,10,11,11,11,11,11,11,11,12,12,12,12,12,13,13,13,13,13,13,13,1,1,1,1,1,1,2,2,2,2,2,2,2,0,0,0]

number = 0

for n in range(10000000):
    owned = {'3':5, 
         '4':3, 
         '5':3,
         '6':0,
         '7':1,
         '8':2,
         '9':0,
         '10':2,
         'J':1,
         'Q':3,
         'K':1,
         'A':2,
         '2':1,
         'JOKER':1}
    chosen = random.sample(range(0,82), 8)
    for i in range(8):
        if unowned[chosen[i]] == 3:
            owned['3']+=1
        elif unowned[chosen[i]] == 4:
            owned['4']+=1
        elif unowned[chosen[i]] == 5:
            owned['5']+=1
        elif unowned[chosen[i]] == 6:
            owned['6']+=1
        elif unowned[chosen[i]] == 7:
            owned['7']+=1
        elif unowned[chosen[i]] == 8:
            owned['8']+=1
        elif unowned[chosen[i]] == 9:
            owned['9']+=1
        elif unowned[chosen[i]] == 10:
            owned['10']+=1
        elif unowned[chosen[i]] == 11:
            owned['J']+=1
        elif unowned[chosen[i]] == 12:
            owned['Q']+=1
        elif unowned[chosen[i]] == 13:
            owned['K']+=1
        elif unowned[chosen[i]] == 1:
            owned['A']+=1
        elif unowned[chosen[i]] == 2:
            owned['2']+=1
        else:
            owned['JOKER']+=1
    bomb = 0
    if owned['3']>=4:
        bomb+=1
    if owned['4']>=4:
        bomb+=1
    if owned['5']>=4:
        bomb+=1
    if owned['6']>=4:
        bomb+=1
    if owned['7']>=4:
        bomb+=1
    if owned['8']>=4:
        bomb+=1
    if owned['9']>=4:
        bomb+=1
    if owned['10']>=4:
        bomb+=1
    if owned['J']>=4:
        bomb+=1
    if owned['Q']>=4:
        bomb+=1
    if owned['K']>=4:
        bomb+=1
    if owned['A']>=4:
        bomb+=1
    if owned['2']>=4:
        bomb+=1
    if owned['JOKER']>=4:
        bomb+=1

    if bomb == 3:
        number = number + 1

print(number)