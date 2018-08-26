#So the question was: Ask the user for 2 numbers and print a
# square of “*”’s that is the width of the first number and the depth of the second number

# What is the width: 3
# What is the depth: 4

# ***
# ***
# ***
# ***

house_rooms = [["Outside", "Living Room"], ["Living Room", "Kitchen"],
                ["Kitchen", "Closet"], ["Kitchen", "Bedroom"],
                ["Bedroom", "Washroom"], ["Washroom", "Attic"]]

starting_room = input("What room do you want to start from? ")
ending_room = input("What room do you want to end in? ")

last_rooms = [""]
last_rooms_index = [0]
len_of_path = 0

current_room_index = 0;

#Loop through all doors and find rooms connected to starting room
while not starting_room == ending_room:
    connected_room = []
    num_connected_rooms = 0

    for room_pairs in house_rooms:
        room1 = room_pairs[0]
        room2 = room_pairs[1]

        last_room = last_rooms[len_of_path]

        if starting_room == room1:
            if not last_room == room2:
                connected_room = connected_room + [room2]
                num_connected_rooms = num_connected_rooms + 1

        if starting_room == room2:
            if not last_room == room1:
                connected_room = connected_room = [room1]
                num_connected_rooms = num_connected_rooms + 1

    if num_connected_rooms == 0:
        #Then we want to go back

        last_room = last_rooms[len_of_path]
        starting_room = last_room
        current_room_index = last_rooms_index[len_of_path]

        #And then subtracted the last one
        new_last_room = []
        new_last_room_index = []

        i = 0
        while i < len_of_path:
            new_last_room = new_last_room + [last_rooms[i]]
            new_last_room_index = new_last_room_index + [last_rooms_index[i]]
            i = i + 1

        len_of_path = len_of_path - 1
        last_rooms = new_last_room

    else:
        #Pick the first room and go into it
        last_rooms = last_rooms + [starting_room]
        len_of_path = len_of_path + 1

        starting_room = connected_room[current_room_index]

        last_rooms_index = last_rooms_index + [current_room_index]

        print("Going into: " + starting_room)
        current_room_index = 0



print("And you have arrived in your last room!")