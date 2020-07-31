import pyautogui


"""
x,y= pyautogui.position()

print(x,y,":",x-60, y-60) # 마우스 위치 좌표 가져오기.

pyautogui.screenshot('1.png', region=(x-60, y-60, 120, 120)) # 해당 좌표를 스크린샷 좌표x, 좌표y, 크기x, 크기y

"""
for count in range(10):    
    i = pyautogui.locateOnScreen('1.png')
    #i = pyautogui.locateCenterOnScreen('8.png')

    pyautogui.click(i)

