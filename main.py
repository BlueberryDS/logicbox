# Master of The Universe - Kavin The God
Entered_Numbers = []
while True:
    num_1 = int(input("What is number 1"))
    num_2 = int(input("What is number 2"))

    sum_1 = num_1 + num_2

    print(sum_1)

    if sum_1 == 100:
        print("3!")
        print("2!")
        print("1!")
        print("KABOOM!!!")

    Entered_Numbers = Entered_Numbers + [num_1, num_2]
    if sum_1 == 0:
        print(Entered_Numbers)
