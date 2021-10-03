


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

def helpChoices(currentRoom: Room):
    print("\n -------------------------")
    print("|                         |")
    print("|  'go' to move           |")
    print("|  'use' to use           |")
    print("|  'fight' to fight       |")
    print("|  'I' for inventory      |")
    print("|  'play' to start game   |")
    print("|  'shop' to enter shop   |")
    print("|                         |")
    print(" -------------------------")

def helpFightChoices(inventory):


def printInventoryChoices(inventory):
    inventoryNames = []
    for i in inventory:
        inventoryNames.append(i.getItem())
    joinedList = " | use ".join(inventoryNames)
    print(f"Choices: | use {joinedList} |")




# Lägg till help så man kan se vad som går att göra baserat på vilket rum man är i




