from logic import *

#Start your program here

a = 1

def b():
    global a
    a += 2
    print( " " + str(a))

b()
print(a)