import pyautogui
import time
import keyboard



delay = 1



def MacroClicker(mac):

    return pyautogui.click(mac)
    





time.sleep(3)

toggle = 0

for i in range(99999999999):
    
    

    if toggle == 0:
        print('게시글 클릭!')

        pyautogui.click(315,300)

        toggle = 1

    else:
        pyautogui.click(620,620)
        toggle = 0
    
     

    


    time.sleep(delay)


    num2 = pyautogui.locateCenterOnScreen('good.png') # 이미지를 불러오기.
    

    if num2 != None:

        print('추천!')
        MacroClicker(num2)

        time.sleep(delay)
    
        print('뒤로가기!')
        pyautogui.press('backspace') 
    
    if num2 == None:

        count = 0

        while True:

            if count==30:
                print('뒤로가기!')
                pyautogui.press('backspace')

                print('페이지 업')
                pyautogui.press('pgup')

                break
                
            
            print('없으므로 페이지 다운')
            pyautogui.press('pgdn')


            num2 = pyautogui.locateCenterOnScreen('good.png') # 이미지를 불러오기.

            count+=1
            
            if num2 != None:

                time.sleep(delay)

                
                num2 = pyautogui.locateCenterOnScreen('good.png') # 이미지를 불러오기.
                print('추천!')
                MacroClicker(num2)


                time.sleep(delay)
                

                print('뒤로가기!')
                pyautogui.press('backspace') 

                break
            
        
        
            




    time.sleep(delay)

    print('F5!')
    pyautogui.press('F5')



    time.sleep(delay)


    i+=1
