import pyautogui


x,y = pyautogui.position()
print(x,y) # 마우스 위치 좌표 가져오기.



#num8 = pyautogui.locateOnScreen('8.png') # 이미지를 불러오기.

#print(num8)


#pyautogui.screenshot('1.png', region=(x-150, y-150, 300, 300)) # 해당 좌표를 스크린샷 좌표x, 좌표y, 크기x, 크기y


num1 = pyautogui.locateCenterOnScreen('1.png') # 이미지를 불러오기.


pyautogui.click(num1) # 마우스 클릭
#pyautogui.click(num8) # 마우스 클릭

