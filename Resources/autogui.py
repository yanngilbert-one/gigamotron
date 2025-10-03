import pyperclip #used to see what was copied.
import pyautogui
import time
#to get this to work on your machine you will open the terminal (can just run the file to get it to open, and in the terminal type "-m pip install pyautogui"), restart vscode after running this to be able to use it
#this is the library we will be using to control the mouse and keyboard, see example below
#for me, the # was between 15% to 9% for X and 35% to 50% for Y, I picked values in between and it is spot on

screen_width, screen_height = pyautogui.size()
#x_percent = 0.17
#y_percent = 0.41
#
#x=int(screen_width * x_percent)
#y=int(screen_height * y_percent)
#
#pyautogui.moveTo(x,y, duration=2)
#
#pyautogui.click()
#
#pyautogui.typewrite("Hello world ")
#
#
#pyautogui.keyDown('shift')
#pyautogui.press('a')
#pyautogui.keyUp('shift')
#time.sleep(1)

def hover_item():
    x_percent_item = 0.174
    y_percent_item = 0.422
    x_item=int(screen_width * x_percent_item)
    y_item=int(screen_height * y_percent_item)
    pyautogui.moveTo(x_item,y_item, duration=0.1)

def copy_item():
    hover_item()

    #pyautogui.rightClick() #Just to select the POE screen for now, otherwise it does not copy item text
    pyautogui.hotkey("ctrl", "c")
    time.sleep(0.5)

def check_clipboard_for(keyword, line_number=3):
    text = pyperclip.paste()
    lines = text.splitlines()
    if len(lines) >= line_number:
        return keyword in lines[line_number - 1]
    return False


    

def use_alt():
    x_percent_alt = 0.057
    y_percent_alt = 0.248
    x_alt=int(screen_width * x_percent_alt)
    y_alt=int(screen_height * y_percent_alt)
    pyautogui.moveTo(x_alt,y_alt, duration=0.1)
    pyautogui.rightClick()
    hover_item()

def use_aug():
    x_percent_aug = 0.117
    y_percent_aug = 0.3
    x_aug=int(screen_width * x_percent_aug)
    y_aug=int(screen_height * y_percent_aug)
    pyautogui.moveTo(x_aug,y_aug, duration=0.1)
    pyautogui.rightClick()
    hover_item()

