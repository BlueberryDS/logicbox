from logic import *

#
#This is a program to solve a single logic box
#

box = get_new_logic_box()
analyser = get_new_analyser()
unlocker = get_new_unlocker()
c=0
o=0

type = analyser.analyse(box)

print("The type of logic box: " + type)

if type == "COMBO":
    while not box.is_unlocked():
        box.flip()
        box.interact("TAP")

    result = unlocker.unbox(box)
    boxlist = result
    print(result)

while not is_game_done():
    if analyser.analyse(boxlist[c]) == "COMBO":
        while not boxlist[c].is_unlocked():
            boxlist[c].flip()
            boxlist[c].interact("TAP")

        boxlist += unlocker.unbox(boxlist[c])
    if analyser.analyse(boxlist[c]) == "OMNI":
        omniNum = c
        o = 1
    if o == 1:
        omni = unlocker.unbox(boxlist[omniNum])
    c += 1

print("IM DONE!!!!")
