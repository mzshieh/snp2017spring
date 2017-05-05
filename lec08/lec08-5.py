# 讀入一個整數，介於0~6之間
# 讀入 0~6 代表週日、週一、...、週六
# try-except-else 版本

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
    break
        
