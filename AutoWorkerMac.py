
#WARNING#

# Please make sure you have 'pynput' installed on your computer. You can do this through the command line terminal by typing "pip install pynput"

# You will have a __ second delay before the program starts. MAKE SURE THAT CHROME and FIGMA are the last two apps opened before it starts

# Enjoy. Please message me for any revisions or questions


import pynput
import time
import random
from pynput.mouse import Button, Controller
from pynput.keyboard import Key, Controller, Listener
keyboard = pynput.keyboard.Controller()
mouse = pynput.mouse.Controller()


def say(word):
    time.sleep(2)
    keyboard.type(word)
def movemouse(x, y):
    time.sleep(1)
    mouse.position = (x,y)
    time.sleep(1)
def click(button):
    mouse.press(button)
    mouse.release(button)
def scroll():
    for i in range(20):
        keyboard.press(Key.down)
        time.sleep(0.1)
    time.sleep(1)
    for i in range(20):
        keyboard.press(Key.up)
        time.sleep(0.1)
        
    time.sleep(0.75)



def first_tab():
    movemouse(84,26)
    click(Button.left)
def second_tab():
    movemouse(247,26)
    click(Button.left)
def third_tab():
    movemouse(410,26)
    click(Button.left)
def fourth_tab():
    movemouse(573,26)
    click(Button.left)




numbers = [1,2,3,4]

keys = [Key.left, Key.right]

def switchwindow():              #switching WINDOW (chrome, figma)
    keyboard.press(Key.cmd)
    keyboard.press(Key.tab)
    keyboard.release(Key.cmd)
    keyboard.release(Key.tab)

def switchingany():              #switching between  tabs
    keyboard.press(Key.ctrl)
    keyboard.press(Key.tab)
    keyboard.release(Key.ctrl)
    keyboard.release(Key.tab)

def randomonpage():               #function for actions within each chrome tab
    for i in range(5):
        movemouse( (random.randrange(300,500)), (random.randrange(300,500)))
        click(Button.left)
        scroll()
        time.sleep(0.5)
        keyboard.press(Key.left)
        keyboard.release(Key.left)
        keyboard.press(Key.right)
        keyboard.release(Key.right)
    
def spamspace():                   #spams space button (for figma)
    for g in range(8):
        keyboard.press(Key.space)
        keyboard.release(Key.space)     


time.sleep(20)                 

def main():                        #mothership, goes to 1st chrome tab, then clicks on the center, does actions and then goes to next tab to repeat
    keyboard.press(Key.cmd)
    keyboard.press('1')
    keyboard.release(Key.cmd)
    keyboard.release('1')

    for x in range(5):                                             
        randomonpage() #centering, scrolling and silent actions
        switchingany() #switching to next chrome tab



def figmaall():                     #within figma, goes to first figma tab, 
    keyboard.press(Key.cmd)
    keyboard.press('2')        #goes to first figma tab
    keyboard.release(Key.cmd)
    keyboard.release('2')

    mouse.position = (660, 408)
    click(Button.left)

    for i in range(10):
        spamspace()
        switchingany()


    
while True:
    main()

    keyboard.press(Key.cmd)
    keyboard.press(Key.tab)
    keyboard.release(Key.cmd)
    keyboard.release(Key.tab)

    figmaall()

    keyboard.press(Key.cmd)
    keyboard.press(Key.tab)
    keyboard.release(Key.cmd)
    keyboard.release(Key.tab)                            #runner
