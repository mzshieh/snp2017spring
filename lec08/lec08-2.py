# 讀入一個整數，介於0~6之間
# 讀入 0~6 代表週日、週一、...、週六
# break 版本
day = int(input('Please enter day (0-6): '))
while True:
    if day <= 6 and day >= 0:
        if day == 0 or day == 6:
            print('no school')
        else:
            print('go to school')
        break
    else:
        print('{} is invalid.'.format(day))
        day = int(input('Please enter day (0-6): '))

        
