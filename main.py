from pynput import mouse
import pyttsx3
import time
import keyboard
from datetime import date, datetime, timedelta
from pynput.keyboard import Key, Listener
from pynput.mouse import Listener

delta = timedelta(
    hours=0,
    seconds=6,
    minutes=0,
)

from pynput.mouse import Listener
engineSlow = pyttsx3.init()
engineFast = pyttsx3.init()

engineFast.setProperty('rate', 900) 
engineFast.setProperty('volume',1.0) 
voices = engineFast.getProperty('voices')   
engineFast.setProperty('voice', voices[1].id)


engineSlow.setProperty('rate', 150) 
engineSlow.setProperty('volume',1.0) 
voices = engineSlow.getProperty('voices')   
engineSlow.setProperty('voice', voices[1].id)

emptyValue = (0,datetime,datetime)

count_arrowRight = emptyValue
count_arrowLeft = emptyValue
count_arrowUP = emptyValue
count_arrowDown = emptyValue
count_space = emptyValue

colorsItems = [("red","apple"), ("orange", "orange"), ("yellow","banana"), ("green", "lime")]
keys = [("up","apple"), ("down", "orange"), ("left", "banana"), ("right", "lime")]

wantToListen = True

while(wantToListen):
    x = input("Want to hear the colors? Y/N: ")
    if x == 'Y' or x == 'y':
        for color in colorsItems:
            engineSlow.say(color[0])
            engineSlow.runAndWait()
    elif x == 'N' or x == 'n':
        break
    else:
        continue
           
def resetValues():
    global count_arrowUP,count_arrowDown, count_arrowRight, count_arrowLeft, count_space
    count_arrowUP = count_arrowDown = count_arrowRight = count_arrowLeft = count_space = emptyValue


results = []

for color in colorsItems:
    engineSlow.say("pick the item that is of color: {}".format(color[0]))
    engineSlow.runAndWait()
    while True:
        if keyboard.read_key() == "up" and count_arrowUP[0] != 2:
            time = datetime.now()
            if count_arrowUP[0] == 0:
                resetValues()
                count_arrowUP = (1,time,0);
                engineFast.say("selected. hold the item to confirm")
                engineFast.runAndWait()
            elif count_arrowUP[0] == 1:
                if time - count_arrowUP[1] > delta:
                    count_arrowUP = (1,time,0)
                    engineFast.say("selected. hold the item to confirm")
                    engineFast.runAndWait()
                else: 
                    startValue = count_arrowUP[1]
                    count_arrowUP = (2,startValue,time)
                    engineFast.say("confirmed")
                    engineFast.runAndWait()
                    for k in keys:
                        if k[0] == "up":
                            results.append((color[0], k[1] == color[1] and "True" or "Maybe you get it next time"))
                    break 
        elif keyboard.read_key() == "down" and count_arrowDown[0] != 2:
            time = datetime.now()
            if count_arrowDown[0] == 0:
                resetValues()
                count_arrowDown = (1,time,0);
                engineFast.say("selected. hold the item to confirm")
                engineFast.runAndWait()
            elif count_arrowDown[0] == 1:
                if time - count_arrowDown[1] > delta:
                    count_arrowDown = (1,time,0)
                    engineFast.say("selected. hold the item to confirm")
                    engineFast.runAndWait()
                else: 
                    startValue = count_arrowDown[1]
                    count_arrowDown = (2,startValue,time)
                    engineFast.say("confirmed")
                    engineFast.runAndWait()
                    for k in keys:
                        if k[0] == "down":
                            results.append((color[0], k[1] == color[1] and "True" or "Maybe you get it next time"))
                    break    
        elif keyboard.read_key() == "left" and count_arrowLeft[0] != 2:
            time = datetime.now()
            if count_arrowLeft[0] == 0:
                resetValues()
                count_arrowLeft = (1,time,0);
                engineFast.say("selected. hold the item to confirm")
                engineFast.runAndWait()
            elif count_arrowLeft[0] == 1:
                if time - count_arrowLeft[1] > delta:
                    count_arrowLeft = (1,time,0)
                    engineFast.say("selected. hold the item to confirm")
                    engineFast.runAndWait()
                else: 
                    startValue = count_arrowLeft[1]
                    count_arrowLeft = (2,startValue,time)
                    engineFast.say("confirmed")
                    engineFast.runAndWait()
                    for k in keys:
                        if k[0] == "left":
                            results.append((color[0], k[1] == color[1] and "True" or "Maybe you get it next time"))
                    break  
        elif keyboard.read_key() == "right" and count_arrowRight[0] != 2:
            time = datetime.now()
            if count_arrowRight[0] == 0:
                resetValues()
                count_arrowRight = (1,time,0);
                engineFast.say("selected. hold the item to confirm")
                engineFast.runAndWait()
            elif count_arrowRight[0] == 1:
                if time - count_arrowRight[1] > delta:
                    count_arrowRight = (1,time,0)
                    engineFast.say("selected. hold the item to confirm")
                    engineFast.runAndWait()
                else: 
                    startValue = count_arrowRight[1]
                    count_arrowRight = (2,startValue,time)
                    engineFast.say("confirmed")
                    engineFast.runAndWait()
                    for k in keys:
                        if k[0] == "right":
                            results.append((color[0], k[1] == color[1] and "True" or "Maybe you get it next time"))
                    break
for r in results:
    engineFast.say("For {} {}".format(r[0],r[1] == "True" and "you did Good" or r[1]))
    engineFast.runAndWait();
    
# Open a file with access mode 'a'
file_object = open('results.txt', 'a')
# Append 'hello' at the end of file
file_object.write(str(results).strip('[]'))
# Close the file
file_object.close()
