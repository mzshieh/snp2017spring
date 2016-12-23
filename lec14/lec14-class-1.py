import random

# check num consists of 4 different digits
def invalid(num):
    num = str(num)
    while len(num)<4:
        num = '0'+num
    for pos in range(4):
        if num[pos] in num[:pos]:
            return True
    return False

# get input
def get_guess():
    while True:
        input_str = input()
        try:
            input_num = int(input_str)
        except:
            continue
        if input_num < 123:
            continue
        if input_num > 9876:
            continue
        if invalid(input_num):
            continue
        return input_num

# count how many A's
def get_a(ans, guess):
    ret = 0
    for i in [1,10,100,1000]:
        if (ans // i) % 10 == (guess // i) % 10:
            ret = ret + 1
    return ret

# count how many B's
def get_b(ans, guess):
    ret = -get_a(ans,guess)
    ans = '%04d' % ans
    guess = '%04d' % guess
    for c in guess:
        if c in ans:
            ret = ret + 1
    return ret

# generate a valid answer
ans = random.randint(123,9876)
while invalid(ans):
    ans = random.randint(123,9876)

# loop until the answer is revealed
while True:
    guess = get_guess()
    a = get_a(ans, guess)
    b = get_b(ans, guess)
    if a == 4 and b == 0:
        # correct answer!
        print('You are correct.')
        break
    else:
        # not correct
        print(str(a)+'A'+str(b)+'B')
