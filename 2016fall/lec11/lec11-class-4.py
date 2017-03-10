import random

secret = random.randint(0,9)
for rnd in range(5):
    x = input('Guess a number: ')
    try:
        x = int(x)
    except:
        print('wrong format')
        continue
    if x == secret:
        print('You know the secret!')
        break
    elif x < secret:
        print('The secret is greater.')
    elif x > secret:
        print('The secret is less.')
