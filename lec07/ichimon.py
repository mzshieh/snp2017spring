#   載入套件
import pyautogui, time

#   關掉安全模式，避免程式在滑鼠滑到左上角時中斷。
pyautogui.FAILSAFE = False

#   按 Windows 鍵：按開始
pyautogui.press('win')

#   輸入 mspaint 後按 Enter 鍵，執行小畫家
pyautogui.typewrite('mspaint')
pyautogui.press('enter')

#   滑鼠跑到左上角，並浪費兩秒鐘。
#   重點是要浪費兩秒鐘等小畫家打開，不然接不上下一個動作。
pyautogui.moveTo(0,0,2)

#   同時按下 Windows 鍵與 上箭頭 鍵，用熱鍵將小畫家最大化。
pyautogui.hotkey('win','up')

# 選畫圈圈
# 找到畫圈圈的工具
loc = pyautogui.locateOnScreen('oval.png')
while loc == None:
    print('oval','not found')
    time.sleep(0.1)
    loc = pyautogui.locateOnScreen('oval.png')
# 點擊
center = pyautogui.center(loc)
pyautogui.click(center)

# 畫圈圈
# 移到左上
pyautogui.moveTo(200,200)
# 拖曳到右下
pyautogui.dragRel(200,200)
# 選畫矩形
# 找到畫的工具
loc = pyautogui.locateOnScreen('rect.png')
while loc == None:
    print('rect','not found')
    time.sleep(0.1)
    loc = pyautogui.locateOnScreen('rect.png')

# 點擊
center = pyautogui.center(loc)
pyautogui.click(center)

# 畫正方形
# 移到左上
pyautogui.moveTo(280,280)
# 拖曳到右下
pyautogui.dragRel(40,40)

# 選填色
# 找到工具
loc = pyautogui.locateOnScreen('fill.png')
while loc == None:
    print('fill','not found')
    time.sleep(0.1)
    loc = pyautogui.locateOnScreen('fill.png')
# 點擊
center = pyautogui.center(loc)
pyautogui.click(center)

# 填色
# 移動到正方形上面一點
pyautogui.moveTo(270,270)
# 點擊
pyautogui.click()
