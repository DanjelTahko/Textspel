from room import Room


def help():
    while True:
        print("\n ------------------------------------------------------------------")
        print("|                                                                  |")
        print("|  write 'go' + 'direction' to move between different rooms        |")
        print("|                                                                  |")
        print("|  write 'use' + 'item in inventory' to use different items        |")
        print("|                                                                  |")
        print("|  write 'fight' to fight enemies in different rooms               |")
        print("|                                                                  |")
        print("|  write 'I' to show inventory                                     |")
        print("|                                                                  |")
        print("|  write 'play' to start games in different romms                  |")
        print("|                                                                  |")
        print("|  write 'shop' to enter shopmenu when current room is shop        |")
        print("|                                                                  |")
        print("|------------------------------------------------------------------|")
        print("|                                                                  |")
        print("|       ** You can always write 'help' to see you choices **       |")
        print("|                                                                  |")
        print(" ------------------------------------------------------------------")
        ok = input("Write 'ok' if you understand: ").lower()
        if ok == 'ok':
            break

def helpChoices(currentRoom: Room, fighting):
    checkEnemy = currentRoom.getEnemy()
    rooms = ['Room 1', 'Room 2', 'Room 3', 'Room 4', 'Room 5']

    if currentRoom.getName() in rooms[:-1] and checkEnemy.getHealth() <= 0:
        print("\n --------------------------- ")
        print("|   Help: Player Choices    |")
        print(" --------------------------- ")
        print("| * Go right                |")
        print("| * Go left                 |")
        print("| * Go back                 |")
        print("| * Use + item in inventory |")
        print("| * 'I' to see inventory    |")
        print(" --------------------------- ")
    
    elif currentRoom.getName() in rooms and checkEnemy.getHealth() > 0 and fighting == False:
        print("\n --------------------------- ")
        print("|   Help: Player Choices    |")
        print(" --------------------------- ")
        print("| * Fight                   |")
        print("| * Go back                 |")
        print("| * Use + item in inventory |")
        print("| * 'I' to see inventory    |")
        print(" --------------------------- ")

    elif currentRoom.getName() == "Room 5" and checkEnemy.getHealth() <= 0:
        print("\n --------------------------- ")
        print("|   Help: Player choices    |")
        print(" --------------------------- ")
        print("| * Go back                 |")
        print("| * Use + item in inventory |")
        print("| * 'I' to see inventory    |")
        print(" --------------------------- ")

    elif currentRoom.getName() == "Bar":
        print("\n --------------------------- ")
        print("|   Help: Player Choices    |")
        print(" --------------------------- ")
        print("| * Go right                |")
        print("| * Go left                 |")
        print("| * Use + item in inventory |")
        print("| * 'I' to see inventory    |")
        print(" --------------------------- ")

    elif currentRoom.getName() == "Shop":
        print("\n --------------------------- ")
        print("|   Help: Player Choices    |")
        print(" --------------------------- ")
        print("| * Shop                    |")
        print("| * Go back                 |")
        print("| * Use + item in inventory |")
        print("| * 'I' to see inventory    |")
        print(" --------------------------- ")

    elif currentRoom.getName() == "Game Room" or currentRoom.getName() == "Black Jack Room":
        print("\n --------------------------- ")
        print("|   Help: Player Choices    |")
        print(" --------------------------- ")
        print("| * Play to start game      |")
        print("| * Go back                 |")
        print("| * Use + item in inventory |")
        print("| * 'I' to see inventory    |")
        print(" --------------------------- ")

    elif fighting == True:
        print("\n --------------------------- ")
        print("|   Help: Player Choices    |")
        print(" --------------------------- ")
        print("| * Use + item in inventory |")
        print("| * 'I' to see inventory    |")
        print(" --------------------------- ")



    







