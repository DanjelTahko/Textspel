


from room import Room


def help():
    print("\n -------------------------")
    print("|                         |")
    print("|  'go' to move           |")
    print("|  'use' to use item      |")
    print("|  'fight' to fight       |")
    print("|  'I' for inventory      |")
    print("|  'play' to start game   |")
    print("|  'shop' to enter shop   |")
    print("|                         |")
    print(" -------------------------")

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



    


    
  





# Lägg till help så man kan se vad som går att göra baserat på vilket rum man är i




