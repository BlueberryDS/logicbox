import random

locked_count = 0


class LogicBox:
    current_side = 0

    def interact(self, action):
        pass

    def flip(self):
        self.current_side = random.randint(0, 5)
        return self.current_side

    def is_unlocked(self):
        pass


class InternalLogicBox(LogicBox):
    opened = False

    def get_message(self):
        pass

    def get_type(self):
        pass


class OmmiBox(InternalLogicBox):
    def interact(self, action):
        if locked_count == 1:
            return "UNLOCKED"
        return "STILL_LOCKED"

    def is_unlocked(self):
        return locked_count == 1

    def get_message(self):
        return "This logic box will automatically unlock when all " \
               "other boxes currently given to you have been unlocked. \n" \
               "No actions taken on this box will have any effect."

    def get_type(self):
        return "OMNI"


class ComboBox(InternalLogicBox):
    taps_wanted = random.randint(1, 6)
    wanted_side = 0

    def interact(self, action):
        if action != "TAP":
            print("Attempted invalid operation on Logic Box!")
            return "INVALID"
        else:
            if self.wanted_side == self.current_side:
                print("You've tapped the correct side!")
                self.wanted_side = random.randint(0, 5)
                self.taps_wanted -= 1
                return str(self.wanted_side)
            else:
                print("You've tapped the wrong side!")
                return "INVALID"

    def is_unlocked(self):
        return self.taps_wanted == 0

    def get_message(self):
        return "This logic box will give you a number when you perform the action \"TAP\" on it. \n" \
               "Flip it to the side that matches the number given to you, and tap. \n" \
               "Repeat this until the box is unlocked. \n" \
               "This box requires " + str(self.taps_wanted) + " taps to open. \n" \
               "It currently needs to be tapped on side: " + str(self.wanted_side)

    def get_type(self):
        return "COMBO"


logic_box_gotten = False


def get_new_logic_box():
    global logic_box_gotten, locked_count

    if logic_box_gotten:
        print("Cannot get more than one logic box!")
        return None

    logic_box_gotten = True
    locked_count += 1

    return ComboBox()


class Unlocker:
    contents = [
                   [ComboBox(), ComboBox()],
                   [OmmiBox(), ComboBox(), ComboBox()],
                   [ComboBox()]
               ]

    story = ["Mathematics is a place", " where you can create", " things that are impossible ",
             " to create in reality"]

    def __init__(self):
        random.shuffle(self.contents)

    def unbox(self, box):
        global locked_count
        if box.opened:
            print("You have already opened this box before!")
            return []
        if box.is_unlocked():
            print("You have just unlocked this box!")
            box.opened = True
            locked_count -= 1

            if len(self.contents):
                ret = self.contents[0]
                self.contents = self.contents[1:]
                locked_count += len(ret)
                print("Now you have " + str(locked_count) + "boxes to open!")
                return ret
            else:
                print("This box was empty!")
                print("You've received part of a quote: " + self.story[0])
                self.story = self.story[1:]
                return []
        else:
            print("The box you just passed in is still locked. Can not unbox!")
            return []


unlocker_gotten = False


def get_new_unlocker():
    global unlocker_gotten

    if unlocker_gotten:
        print("Can only get one unlocker!")
        return None

    unlocker_gotten = True

    return Unlocker()


class Analyser:
    def analyse(self, box):
        print(box.get_message())
        return box.get_type()


    analyser_gotten = False


def get_new_analyser():
    global analyser_gotten

    if analyser_gotten:
        print("Can only get one Analyser!")
        return None

    analyser_gotten = True

    return Analyser()


def is_game_done():
    global locked_count

    if locked_count > 0:
        print("There are still " + str(locked_count) + " boxes to unlock!")
        return False

    print("Game is done!")
    return True
