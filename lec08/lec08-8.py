import trexutil
# from trexutil import screenshot

import pyautogui, time
### 找恐龍
loc = pyautogui.locateOnScreen('trex.png')
while loc == None:
    print('trex','not found')
    time.sleep(0.1)
    loc = pyautogui.locateOnScreen('trex.png')
### 找到後按一下空白 開始遊戲
pyautogui.press('space')

### 看到障礙物 就按空白
while True:
    ### 只看 (426,355)~(511,385) 這塊有沒有灰色 (83,83,83)
    im = trexutil.screenshot(region=(426,355,85,30)).im
    if (83,83,83) in im:
        pyautogui.press('space')
    ### 給點時間按 ctrl+c 結束程式
    time.sleep(0.01)
