from logic import *

#
# this is a project to solve a single logic box
#

box = get_new_logic_box()
analyser = get_new_analyser()
unlocker = get_new_unlocker()

type = analyser.analyse(box)
if type == "COMBO":
    while not box.is_unlocked():
        box.flip()
        box.interact("TAP")

    results = unlocker.unbox(box)
    print(results)