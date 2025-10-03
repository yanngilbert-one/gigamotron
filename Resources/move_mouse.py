import pyautogui
import time
#to get this to work on your machine you will open the terminal (can just run the file to get it to open, and in the terminal type "-m pip install pyautogui"), restart vscode after running this to be able to use it
#this is the library we will be using to control the mouse and keyboard, see example below
#for me, the # was between 15% to 9% for X and 35% to 50% for Y, I picked values in between and it is spot on

screen_width, screen_height = pyautogui.size()
x_percent = 0.17
y_percent = 0.41

x=int(screen_width * x_percent)
y=int(screen_height * y_percent)

pyautogui.moveTo(x,y, duration=2)

pyautogui.click()

pyautogui.typewrite("Hello world ")


pyautogui.keyDown('shift')
pyautogui.press('a')
pyautogui.keyUp('shift')
time.sleep(1)