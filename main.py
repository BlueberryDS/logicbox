from logic import *

# This is a program to solve a single logic box

box = get_new_logic_box()
analyser = get_new_analyser()
unlocker = get_new_unlocker()

type = analyser.analyse(box)
index = 0
list_of_content = []

print("The type of box is " + type)

if type == "COMBO":
    while not box.is_unlocked():
        box.flip()
        box.interact("TAP")
    list_of_content.append(unlocker.unbox(box))

while not is_game_done():

    for boxes in list_of_content[index]:

        type = analyser.analyse(boxes)
        print("The type of box is " + type)

        if type == "COMBO":
            while not boxes.is_unlocked():
                boxes.flip()
                boxes.interact("TAP")
            list_of_content.append(unlocker.unbox(boxes))

        elif type == "OMNI":
            list_of_content.append(unlocker.unbox(boxes))
        print(list_of_content)

    for content in list_of_content:

        for boxes in content:

            type = analyser.analyse(boxes)

            if type == "COMBO":
                list_of_content.append(unlocker.unbox(boxes))

            elif type == "OMNI":
                list_of_content.append(unlocker.unbox(boxes))

    index += 1
