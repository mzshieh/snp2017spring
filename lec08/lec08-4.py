# 讀入一個整數，介於0~6之間
# 讀入 0~6 代表週日、週一、...、週六
# try-except-else 版本

while True:
    try:
        day = int(input('Please enter day (0-6): '))
    except ValueError:
        print('Input cannot be converted to int')
        continue
    except KeyboardInterrupt:
        print('Control+C is pressed')
        break
    except:
        print('Exception happened')
    else:
        print("{} is an integer.".format(day))
    if day <= 6 and day >= 0:
        if day == 0 or day == 6:
            print('no school')
        else:
            print('go to school')
        break
    else:
        print('{} is invalid.'.format(day))

        
