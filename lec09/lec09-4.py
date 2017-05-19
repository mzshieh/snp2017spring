from itertools import combinations
from itertools import permutations
import random

# Check whether a input is valid
def valid(s):
    if len(s)!=4:
        return False
    if any(x not in '0123456789' for x in s):
        return False
    if any(x==y for x, y in combinations(s,2)):
        return False
    return True

# Read string which has four distinct digits
def read_four_distinct_digits():
    while True:
        ret = input('Input four distinct digits: ')
        if valid(ret):
            return ret
        print(ret,'is not valid.')

compute_A = lambda guess, ans: sum(1 for x,y in zip(guess,ans) if x==y)
compute_B = lambda guess, ans: sum(1 for x in guess if x in ans)-compute_A(guess,ans)

cand = [''.join(lst) for lst in permutations('0123456789',4)]
history = []
while True:
    guess = read_four_distinct_digits()
    A = int(input('A: '))
    B = int(input('B: '))
    history = history + [(guess,A,B)]
    cand = [x for x in cand if all(compute_A(x,guess)==A and compute_B(x,guess)==B for guess,A,B in history)]
    print(random.choice(cand))
    if A == 4:
        break

