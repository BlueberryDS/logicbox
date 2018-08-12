from logic import *

#
# This is a program to solve logic box
#
box = get_new_logic_box()
analyser = get_new_analyser()
unlocker = get_new_unlocker()

print(analyser.analyse(box))

type_of_box = analyser.analyse(box)
if type_of_box == "COMBO":
    while not box.is_unlocked():
        box.flip()
        box.interact("TAP")
    content = unlocker.unbox(box)
    print(content)
