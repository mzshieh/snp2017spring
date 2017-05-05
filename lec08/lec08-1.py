# 讀入 0~6 代表週日、週一、...、週六
day = int(input('Please enter day (0-6): '))

print('Buggy version:')
if day == 0 or 6:
    print('no school')
else:
    print('go to school')
# 印空白行
print()

print('Correct version:')
if day == 0 or day == 6:
    print('no school')
else:
    print('go to school')
