Entered_Numbers =[]

while True:
    num1 = int(input("Enter number after this: "))
    num2 = int(input("Enter number after this: "))
    total = num1 + num2

    if total == 100:
        print("boom!")
    Entered_Numbers = Entered_Numbers + [num1,num2]
    if total == 0:
        print(Entered_Numbers)