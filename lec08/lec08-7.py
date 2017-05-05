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

# 選工具
def selectTool(name):
    # 找位置
    loc = pyautogui.locateOnScreen('{}.png'.format(name))
    while loc == None:
        print(name,'not found')
        time.sleep(0.1)
        loc = pyautogui.locateOnScreen('{}.png'.format(name))
    # 點擊
    center = pyautogui.center(loc)
    pyautogui.click(center)    

def draw(x,y,w,h):
    pyautogui.moveTo(x,y)
    pyautogui.dragRel(w,h)

def ichimon(x,y,w,h):
    # 選畫圈圈的工具
    selectTool('oval')
    # 畫圈圈
    draw(250,250,100,100)
    # 選畫矩形的工具
    selectTool('rect')
    # 畫正方形
    draw(280,280,40,40)
    # 選填色工具
    selectTool('fill')
    # 點擊
    pyautogui.click(270,270)

ichimon(250,250,100,100)
