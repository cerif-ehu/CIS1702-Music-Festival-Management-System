'''
This code is used to manage the stage information.
'''

while True:

    file = open("data.txt", "r")

    data = file.readlines()
    stage_names = data[1].strip().split(",")
    capacity = data[4].strip().split(",")

    mainchoice = int(input("Enter 1 to add stage information, 2 to view stage information, 3 to update stage information, 4 to delete stage information, 5 to exit: "))
    if mainchoice == 1:
        print(stage_names, capacity)