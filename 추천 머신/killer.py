import keyboard #Using module keyboard
import os

while True:#making a loop
       if keyboard.is_pressed('9'): #if key 'a' is pressed 
           print('You Pressed A Key!')

           os.system('taskkill /im py.exe')
               
