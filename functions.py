from character import Character
from enemyCharacter import EnemyCharacter
from room import Room
import functionsText as text
import shop

# Skapar världen med rum och enemies
def createWorld():

    bar = Room("Bar")
    firstRoom = Room("Room 1")
    secondRoom = Room("Room 2")
    thirdRoom = Room("Room 3")
    fourthRoom = Room("Room 4")
    fifthRoom = Room("Room 5")
    shop = Room("Shop")
    game = Room("Game Room")
    bj = Room("Black Jack Room")
    hangmanRoom = Room("Hangman Room")
    trap = Room("Trap")

    air = EnemyCharacter('Air', 0, 0, 0)
    drunkman = EnemyCharacter('drunkman', 10, 0, 2)
    skeleton = EnemyCharacter('skeleton', 25, 2, 5)
    ninja = EnemyCharacter('ninja', 40, 5, 10)
    beholder = EnemyCharacter('beholder', 1000, 50, 100)

    bar.setRoomtoRight(firstRoom)
    bar.setRoomtoLeft(shop)  # Vänstar om BAR - Shop
    bar.setEnemytoRoom(air)  # //// Enemy till BAR - Air
    shop.setRoomToBack(bar)  # Back om Shop - Bar
    shop.setEnemytoRoom(air)

    firstRoom.setRoomtoRight(game)  # Höger om Room 1 - Game Room
    firstRoom.setRoomtoLeft(secondRoom)  # Vänster om Room 1 - Room 2
    firstRoom.setRoomToBack(bar)  # Back om Room 1 - Bar
    firstRoom.setEnemytoRoom(drunkman)  # Enemy to room (Drunkman)
    game.setRoomToBack(firstRoom)  # Back om Game Room - Room 1
    game.setEnemytoRoom(air)  # //// Enemy till Game Room - Air

    secondRoom.setRoomtoLeft(trap)  
    secondRoom.setRoomtoRight(thirdRoom)  # Höger om Room 2 - Room 3
    secondRoom.setRoomToBack(firstRoom)  # Back om Room 2 - Room 1
    secondRoom.setEnemytoRoom(skeleton)  # Enemy to room (Skeleton)

    thirdRoom.setRoomtoRight(hangmanRoom)
    thirdRoom.setRoomtoLeft(fourthRoom)
    thirdRoom.setRoomToBack(secondRoom)
    thirdRoom.setEnemytoRoom(ninja)  # Enemy to Room (Ninja)

    fourthRoom.setRoomtoRight(bj)
    fourthRoom.setRoomtoLeft(fifthRoom)
    fourthRoom.setRoomToBack(thirdRoom)
    fourthRoom.setEnemytoRoom(EnemyCharacter('skeleton', 50, 2, 5))

    bj.setRoomToBack(fourthRoom)
    bj.setEnemytoRoom(air)

    fifthRoom.setRoomToBack(fourthRoom)
    fifthRoom.setEnemytoRoom(beholder)

    hangmanRoom.setRoomToBack(thirdRoom)
    trap.setRoomToBack(bar)

    return bar

# Ändrar rum beroende på vart man går (right, left, back)
def getRoomInDirection(currentRoom: Room, direction):

    if direction == "right" and currentRoom.getEnemy().getHealth() <= 0:
        return currentRoom.getRoomToRight()

    elif direction == "left" and currentRoom.getEnemy().getHealth() <= 0:
        return currentRoom.getRoomToLeft()

    elif direction == "back":
        return currentRoom.getRoomToBack()

# Kollar om valet USE finns i inventory och returnar ITEM
def useItem(itemInput, inventory):

    # Om det tillexempel är "use large health"
    if len(itemInput) > 2:
        choice = " ".join(itemInput[1:3])
    else:
        # Om det tillexempel är "use fist"
        choice = itemInput[1]
                
    inventoryStrings = shop.getItemsFromInventory(inventory)
    if choice in inventoryStrings:
        index = inventoryStrings.index(choice)
        return inventory[index]


def fightMode(currentRoom: Room, player: Character, inventory):

    fightEnemy = currentRoom.getEnemy()

    while fightEnemy.getHealth() > 0 and player.getHealth() > 0:

        text.printFightState(fightEnemy, player)
        command = input("What do you wish to do? ").lower()
        subcommands = command.split(" ")

        if subcommands[0] == "use":

            item = useItem(subcommands, inventory)

            if item == None:
                print("You are unable to " + command)

            else:
                text.printPlayerUsing(item, player, inventory)
                #fight bara ifall man inte använder en potion
                if item.getMaxDamage() > 0 and player.getCriticalDamage() == False:
                    print(f"* You attack for: {item.setDamage()} dmg")
                    fightEnemy.takeDamage(item.getDamage())
                    if fightEnemy.getHealth() > 0:
                        print(
                            f"* {fightEnemy.getName()} attacks for: {fightEnemy.setDamage()} dmg")
                        player.takeDamage(fightEnemy.getDamage())

                elif item.getMaxDamage() > 0 and player.getCriticalDamage() == True:
                    print(f"* You attack for: {item.getMaxDamage()} dmg")
                    fightEnemy.takeDamage(item.getMaxDamage())
                    if fightEnemy.getHealth() > 0:
                        print(
                            f"* {fightEnemy.getName()} attacks for: {fightEnemy.setDamage()} dmg")
                        player.takeDamage(fightEnemy.getDamage())

        elif command == "i":
            text.printInvetory(inventory)
        
        elif command == "help":
            text.printHelpChoices(currentRoom, True)

    if fightEnemy.getHealth() <= 0:
        print(f"You killed {fightEnemy.getName()}")
        text.printWhenEnemyKilled(fightEnemy.getName(), player)
        if player.getCriticalDamage() == True:
            player.removeCriticalDamage()

