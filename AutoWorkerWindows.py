
#WARNING#

# Please make sure you have 'pynput' installed on your computer. You can do this through the command line terminal by typing "pip install pynput"

# You will have a 10 second delay before the program starts. MAKE SURE THAT CHROME and FIGMA are the last two apps opened before it starts

# Enjoy. Please message me for any revisions or questions



import pynput
import time
import random
from pynput.mouse import Button, Controller
from pynput.keyboard import Key, Controller 
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
    time.sleep(1)
    for i in range(20):
        keyboard.press(Key.up)
        
    time.sleep(0.75)
def switchwindow():
    keyboard.press(Key.ctrl)
    keyboard.press(Key.tab)
    keyboard.release(Key.ctrl)
    keyboard.release(Key.tab)


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
keylist = ["a", "e", "i", "o", "u", Key.space]
keys = [Key.left, Key.right]

def randomonpage():
    for i in range(random.choice(numbers)):
        scroll()
        keyboard.press(random.choice(keylist))

time.sleep(10)
def main():
    assign = random.choice(numbers)
    if assign == 1:
        first_tab()
        movemouse(500,500)
        click(Button.left)
        randomonpage()
    elif assign == 2:
        second_tab()
        movemouse(500,500)
        click(Button.left)
        randomonpage()
    elif assign == 3:
        third_tab()
        movemouse(500,500)
        click(Button.left)
        randomonpage()
    elif assign == 4:
        fourth_tab()
        movemouse(500,500)
        click(Button.left)
        randomonpage()


def figmarunning():
    for x in range(8):
        movemouse((random.randrange(5,990)), random.randrange(20, 990))
        click(Button.left)
        keyboard.press(Key.space)
        keyboard.release(Key.space)
    
    
while True:
    main()
    main()
    switchwindow()
    figmarunning()
    switchwindow()
    main()
    main()