import pyautogui
import time

x,y = pyautogui.position()
print(x,y) # 마우스 위치 좌표 가져오기.



#num8 = pyautogui.locateOnScreen('8.png') # 이미지를 불러오기.

#print(num8)


#pyautogui.screenshot('2.png', region=(x-25, y-25, 50, 50)) # 해당 좌표를 스크린샷 좌표x, 좌표y, 크기x, 크기y





num1 = pyautogui.locateCenterOnScreen('1.png') # 이미지를 불러오기.
print('1클릭',num1)
pyautogui.click(num1) # 마우스 클릭

time.sleep(1)


num2 = pyautogui.locateCenterOnScreen('2.png') # 이미지를 불러오기.
print('2클릭',num2)
pyautogui.click(num2) # 마우스 클릭

