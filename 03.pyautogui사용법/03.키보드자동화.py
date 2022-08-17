import pyautogui
import time

# 1. 키보드 입력(문자)
# pyautogui.write('startcoding')

# pyautogui.write('startcoding',interval=0.25)

#pyautogui.write('스타트코딩') # 한글은 안됨


# 2. 키보드입력(키)
# pyautogui.press('enter') #엔터키 누르기
# pyautogui.press('hangul')   # 한영키

# time.sleep(2)
# pyautogui.press('hanja')

# 3.키보드 입력(여러 키를 동시에)
# pyautogui.keyDown('ctrl')    #컨트롤 누른상태에서
# pyautogui.press('v')         # 브이 눌러라
# pyautogui.keyUp('ctrl')      # 컨트롤 누른거 뗴라

# pyautogui.hotkey('ctrl','v')   

# 4. 한글입력방법
import pyperclip

pyperclip.copy('#즐거운 불금!!!')    #클립보드에 복사하기
pyautogui.hotkey('ctrl','v')
#즐거운 불금!!!