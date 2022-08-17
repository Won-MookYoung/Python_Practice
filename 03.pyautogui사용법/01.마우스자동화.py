import pyautogui
import time
# print(pyautogui.size())              #화면 사이즈

# print(pyautogui.position())           #현재 커서위치


#pyautogui.moveTo(300,400,2)

# import pyautogui, sys                     #마우스 움직일때마다 좌표나타내기
# print('Press Ctrl-C to quit.')
# try:
#     while True:
#         x, y = pyautogui.position()
#         positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
#         print(positionStr, end='')
#         print('\b' * len(positionStr), end='', flush=True)
# except KeyboardInterrupt:
#     print('\n')
    

# pyautogui.onScreen(0, 0)
# print(pyautogui.onScreen(0, -1))   # 커서가 화면 크기안에 위치하는가? true or false
# print(pyautogui.size())
# pyautogui.moveTo(1000, 0)            #x=1000 y-0 좌표로 이동
# pyautogui.moveTo(100, 200, 1)


# pyautogui.moveTo(100, 200)  # moves mouse to X of 100, Y of 200.
# pyautogui.move(0, 50)       # move the mouse down 50 pixels.
# pyautogui.move(-30, 0)      # move the mouse left 30 pixels.
# pyautogui.move(-30, None)   # move the mouse left 30 pixels.

# pyautogui.dragTo(100, 200, button='left')     # drag mouse to X of 100, Y of 200 while holding down left mouse button
# pyautogui.dragTo(300, 400, 2, button='left')  # drag mouse to X of 300, Y of 400 over 2 seconds while holding down left mouse button
# pyautogui.drag(30, 0, 2, button='right')   # drag the mouse left 30 pixels over 2 seconds while holding down the right mouse button

# pyautogui.moveTo(100, 100, 2, pyautogui.easeInQuad)     # start slow, end fast
# pyautogui.moveTo(100, 100, 2, pyautogui.easeOutQuad)    # start fast, end slow
# pyautogui.moveTo(100, 100, 2, pyautogui.easeInOutQuad)  # start and end fast, slow in middle
# pyautogui.moveTo(100, 100, 2, pyautogui.easeInBounce)   # bounce at the end
# pyautogui.moveTo(100, 100, 2, pyautogui.easeInElastic)  # rubber band at the end

# pyautogui.click()   # click the mouse

# pyautogui.click(x=100, y=200)  # move to 100, 200, then click the left mouse button.
# pyautogui.click(button='right')  # right-click the mouse

# pyautogui.click(clicks=2)  # double-click the left mouse button
# pyautogui.click(clicks=2, interval=0.25)  # double-click the left mouse button, but with a quarter second pause in between clicks
# pyautogui.click(button='right', clicks=3, interval=0.25)  ## triple-click the right mouse button with a quarter second pause in between clicks

# pyautogui.doubleClick()  # perform a left-button double click

# pyautogui.mouseDown(); pyautogui.mouseUp()  # does the same thing as a left-button mouse click
# pyautogui.mouseDown(button='right')  # press the right button down
# pyautogui.mouseUp(button='right', x=100, y=200)  # move the mouse to 100, 200, then release the right button up.


# pyautogui.scroll(10)   # scroll up 10 "clicks"
# pyautogui.scroll(-10)  # scroll down 10 "clicks"
# pyautogui.scroll(10, x=100, y=100)  # move mouse cursor to 100, 200, then scroll up 10 "clicks"


# pyautogui.hscroll(10)   # scroll right 10 "clicks"
# pyautogui.hscroll(-10)   # scroll left 10 "clicks"

a=pyautogui
# 화면의 크기
# print(a.size())

#마우스의 위치
# time.sleep(2)     #2초 뒤의 마우스위치 (2초동안 x)
# print(a.position())

#마우스 이동
# a.moveTo(1200,1600)
# a.moveTo(1350,500,2)
a.moveTo(2011,134,2)  #색
a.click(clicks=2,interval=0.5)
a.moveTo(1504,564,2)


#놓기
a.mouseDown()
a.moveTo(1504,564,2)
a.moveTo(1800,564,2)
a.moveTo(1800,910,2)
a.moveTo(1504,910,2)
a.moveTo(1504,564,2)
