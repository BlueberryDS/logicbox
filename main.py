from logic import *

#Start your program here

results = []

while True:
    num1 = int(input("What is the first number? "))
    num2 = int(input("What is the second number? "))
    sums = num1 + num2
    results = results + [sums]
    print(sums)

    condition = sums == 100
    condition2 = sums == 0

    if condition:
        print("Boom!")

    if condition2:
        print(results)