import pyautogui
import time
#to get this to work on your machine you will open the terminal (can just run the file to get it to open, and in the terminal type "-m pip install pyautogui")
#this is the library we will be using to control the mouse and keyboard, see example below

pyautogui.moveTo(500,500, duration=2)

pyautogui.click()

pyautogui.typewrite("Hello world ")


pyautogui.keyDown('shift')
pyautogui.press('a')
pyautogui.keyUp('shift')
time.sleep(1)