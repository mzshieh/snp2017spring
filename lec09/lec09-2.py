# Read an integer which is in {0,...,9}
def read_a_digit():
    ret = -1
    while True:
        try:
            ret = int(input('Input a digit: '))
        except ValueError:
            print('Not an integer')
            continue
        if ret >= 0 and ret <= 9:
            return ret
        print(ret,'is not in {0,...,9}.')

from random import randint

ans = randint(0,9)

guess = read_a_digit()
while guess != ans:
    if ans < guess:
        print(guess,'is greater than the answer.')
    else:
        print(guess,'is less than the answer.')
    guess = read_a_digit()

print('Congrats! The answer is',ans)
