def my_round(a):
    if a < 0: # int(a) is ceil(a)
        if int(a)-a<0.5:
            return int(a)
        elif int(a)-a>0.5:
            return int(a)-1
        else:
            if int(a) % 2 == 0:
                return int(a)
            else:
                return int(a)-1
        
    elif a > 0: # int(a) is floor(a)

        if a-int(a)<0.5:
            return int(a)
        elif a-int(a)>0.5:
            return int(a)+1
        else:
            if int(a)%2 == 0:
                return int(a)
            else:
                return int(a)+1
        
    else: # a == 0
        return 0

while True:
    x = input('Input a number x: ')
    try:
        x = float(x)
    except:
        if x == 'end':
            break
        print('Wrong format')
        continue
    print('my_round(x):',my_round(x))
    print('round(x):',round(x))










    
