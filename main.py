sum_list = []

while True:
    number_1 = int(input ("What is number 1"))
    number_2 = int(input ("What is number 2"))
    print(number_1 + number_2)
    answer = (number_1 + number_2)
    if answer != 0:
        sum_list.append(answer)
    if answer == 0:
        for y in sum_list:
            print(y)
    if answer == 100:
        print("Boom!")
