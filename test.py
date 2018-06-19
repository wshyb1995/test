import codey
import random

x = 0
list = []

def on_button_callback():
    global x
    x = random.randint(1, 36)
    if  x in list:
        x = random.randint(1, 36)

    else:
        codey.show(x)
        codey.say('score.wav')
        list.append(x)

codey.on_button('A', on_button_callback)



if codey.is_shaked():
    while not not True:





