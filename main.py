
list_of_sums = []

while True:

    print("Enter you First number")
    number_1 = int(input("Age: "))

    print("Enter you Second number")
    number_2 = int(input("Age: "))

    num_Sum = number_1 + number_2

    print("The sum is: " + str(num_Sum))

    list_of_sums = list_of_sums + [num_Sum]

    if num_Sum >= 100:
        print("BOOOOM")

    elif num_Sum == 0:
        for item in list_of_sums:
            print(item)



