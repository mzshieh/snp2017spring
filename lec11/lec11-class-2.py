import pyautogui

def open_mspaint():
    pyautogui.hotkey('win','r')
    pyautogui.typewrite('mspaint')
    pyautogui.press('enter')

open_mspaint()
