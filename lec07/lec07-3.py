import time
from PIL import Image
from mss import mss

# Fast screenshot
# Usage just like pyautogui
# Parameter:
#     region: optional, four-integer tuple (left, top, width, height)
def screenshot(region=None):
    im = None
    monitors = None
    
    with mss() as sct:
        # Retrieve monitors informations:
        monitors = sct.enum_display_monitors()

        # Region to capture
        monitor = dict(monitors[1])
        if region != None:
            monitor['left'] = int(region[0])
            monitor['top'] = int(region[1])
            monitor['width'] = (int(region[2]) // 80 + int(region[2] % 80 != 0)) * 80
            monitor['height'] = int(region[3])

        # Get pixels on image
        sct.get_pixels(monitor)
        im = Image.frombytes('RGB', (sct.width, sct.height), sct.image)

    if monitor['width'] != region[2]:
        im = im.crop((0, 0, region[2], region[3]))

    return im


# Evaluate screenshot time in seconds
def evaluate_screenshot_time(region=None):
    t = time.time()
    im = screenshot(region)
    return time.time() - t

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
    im = screenshot(region=(426,355,85,30)).im
    if (83,83,83) in im:
        pyautogui.press('space')
    ### 給點時間按 ctrl+c 結束程式
    time.sleep(0.01)