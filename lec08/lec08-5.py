# 讀入一個四位整數，可以0開頭，但位數不可重複使用相同數字

while True:
    num = input('Enter a 4-digit number: ')
    if len(num) != 4:
        print('The length is incorrect.')
        continue
    repeated = False
    for i in range(4):
        if num[i] in num[i+1:]:
            repeated = True
            break
    if repeated:
        print('Some digit repeats.')
        continue
    try:
        num = int(num)
    except ValueError:
        print('Input is not an integer.')
        continue
    if num < 123 or num > 9876:
        print('It is invalid')
    print('It is valid.')
    break