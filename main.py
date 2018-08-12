from logic import *

# This is a program to solve a single logic box

box = get_new_logic_box()
analyser = get_new_analyser()
unlocker = get_new_unlocker()

type = analyser.analyse(box)

print("The type of box is " + type)

if type == "COMBO":
    while not box.is_unlocked():
        box.flip()
        box.interact("TAP")
    content = unlocker.unbox(box)
    print(content)