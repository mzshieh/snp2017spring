import random

# check num consists of 2 different digits
def invalid(num):
    return num // 10 == num % 10

# get input
def get_guess():
    while True:
        input_str = input()
        try:
            input_num = int(input_str)
        except:
            continue
        if input_num < 1:
            continue
        if input_num > 98:
            continue
        if invalid(input_num):
            continue
        return input_num

# count how many A's
def get_a(ans, guess):
    ret = 0
    if ans // 10 == guess // 10:
        ret = ret + 1
    if ans % 10 == guess % 10:
        ret = ret + 1
    return ret

# count how many B's
def get_b(ans, guess):
    ret = 0
    if ans // 10 == guess % 10:
        ret = ret + 1
    if ans % 10 == guess // 10:
        ret = ret + 1
    return ret

# generate a valid answer
ans = random.randint(1,98)
while invalid(ans):
    ans = random.randint(1,98)

# loop until the answer is revealed
while True:
    guess = get_guess()
    a = get_a(ans, guess)
    b = get_b(ans, guess)
    if a == 2 and b == 0:
        # correct answer!
        print('You are correct.')
        break
    else:
        # not correct
        print(str(a)+'A'+str(b)+'B')

