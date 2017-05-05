# counter: number of odds read
cnt = 0
# a list storing 5 integers
lst = [0,0,0,0,0]
print('I need five odd numbers.')
while cnt < 5:
    lst[cnt] = int(input('Input an odd number: '))
    if lst[cnt] % 2 == 0:
        print('{} is even.'.format(lst[cnt]))
        continue
    # move to next position in the next round
    cnt = cnt + 1
# print the numbers
print('You gave me {},{},{},{},{}.'.format(*lst))
