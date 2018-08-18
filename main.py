from logic import *

logic_box = get_new_logic_box()
analyser = get_new_analyser()
unlocker = get_new_unlocker()

boxes_to_delete = 0
# The amount of boxes that've been unlocked and that will be deleted
currently_deleting_box = 0


# This is a function to unlock the box
def combo_opener(box):
    while not box.is_unlocked():
        box.flip()
        box.interact("TAP")
    content = unlocker.unbox(box)
    return content
    pass


new_content = combo_opener(logic_box)
my_total_list = new_content

omni_box = logic_box
while not is_game_done():

    currently_deleting_box = 0

    # This prints out the new content list and the entire list
    print("New Content: " + str(new_content))
    print("All together: " + str(my_total_list))

    # This sees how many boxes is in the list for the for loop
    max_boxes = len(my_total_list)

    for boxes in range(max_boxes):
        print("\nAnalysing box " + str(boxes + 1) + " out of " + str(max_boxes))
        result = analyser.analyse(my_total_list[boxes])

        if result == "COMBO":
            new_content = combo_opener(my_total_list[boxes])
            my_total_list.extend(new_content)
            print("Just received: " + str(new_content))
            print("Extending my total list of boxes: " + str(my_total_list))
            boxes_to_delete += 1

        elif result == "OMNI":
            omni_box = my_total_list[boxes]
            print(omni_box)
            boxes_to_delete += 1

    for x in range(boxes_to_delete):
        # This will delete boxes already unlocked
        print(" \nAmount of boxes before deleting:" + str(my_total_list))
        # This checks if the list is empty, so it won't give me an error
        if my_total_list:
            # This check is the box that's currently being deleted is actually unlocked
            if my_total_list[currently_deleting_box].is_unlocked():
                print("Deleted " + str(x) + " box")
                del my_total_list[0]

    if len(my_total_list) == 0 and len(new_content) == 0:
        # If both lists are empty, that means all boxes SHOULD be unlocked, so now I have to unlock the OmniBox
        print("\nBoth lists are empty. All boxes are unlocked except the OmniBox")
        if not omni_box == logic_box:
            # This checks if we've actually encountered a logic box
            unlocker.unbox(omni_box)


