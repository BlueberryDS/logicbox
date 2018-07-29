# Master of The Universe - Kavin The God
r = []
while True:
    num_1 = int(input("What is number 1"))
    num_2 = int(input("What is number 2"))

    sum_1 = num_1 + num_2

    print(sum_1)

    condition = sum_1 == 100
    if condition:
        print("3!")
        print("2!")
        print("1!")
        print("KABOOM!!!")

    r = r + [sum_1]
    cond2 = sum_1 == 0
    if cond2:
        print(r)
