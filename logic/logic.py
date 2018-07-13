import random

unlocked_count = 0
story = "Mathematics is a place where you can do things that you can't do in the real world".split(" ");


class LogicBox:
    current_side = 0

    def interact(self, action):
        pass

    def flip(self):
        self.current_side = random.randint(0, 6)
        return self.current_side

    def is_unlocked(self):
        pass


class InternalLogicBox(LogicBox):
    def get_message(self):
        pass

    def get_type(self):
        pass


class OmmiBox(InternalLogicBox):
    def interact(self, action):
        if unlocked_count == 0:
            return "UNLOCKED"
        return "STILL_LOCKED"

    def is_unlocked(self):
        return unlocked_count == 0

    def get_message(self):
        return "This logic box will automatically unlock when all " \
               "other boxes currently given to you have been unlocked. \n" \
               "No actions taken on this box will have any effect."

    def get_type(self):
        return "OMNI"


class ComboBox(InternalLogicBox):
    taps_wanted = random.randint()
    wanted_side = 0

    def interact(self, action):
        if action != "TAP":
            print("Attempted invalid operation on Logic Box!")
            return "INVALID"
        else:
            if self.wanted_side == self.current_side:
                print("You've tapped the correct side!")
                self.wanted_side = random.randint(0, 6)
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


class Unlocker:
    def unbox(self, box):
        if box.is_unlocked():
            print("You have just unlocked this box!")
        else:
            print("The box you just passed in is still locked. Can not unbox!")


class Analyser:
    def analyse(self, box):
        print(box.get_message())
        return box.get_type()


def get_new_analyser():
    return Analyser()
