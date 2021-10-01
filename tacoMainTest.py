from room import Room
from item import Item
from enemyCharacter import EnemyCharacter
from character import Character
from mastermind import MasterMind
from gubee import Hangman
import random


def createWorld():
    bar = Room("Bar")
    firstRoom = Room("Room 1")
    secondRoom = Room("Room 2")
    thirdRoom = Room("Room 3")
    fourthRoom = Room("Room 4")
    fifthRoom = Room("Room 5")
    shop = Room("Shop")
    game = Room("Game Room")
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

    fourthRoom.setRoomtoRight(fifthRoom)
    fourthRoom.setRoomtoLeft(fifthRoom)
    fourthRoom.setRoomToBack(thirdRoom)
    fourthRoom.setEnemytoRoom(EnemyCharacter('skeleton', 50, 2, 5))

    fifthRoom.setRoomToBack(fourthRoom)
    fifthRoom.setEnemytoRoom(beholder)

    hangmanRoom.setRoomToBack(thirdRoom)
    trap.setRoomToBack(bar)

    return bar

# Kollar om valet USE finns i inventory och returnar ITEM


def useItem(choice, inventory):
    if choice == "fist" and fist in inventory:
        return fist
    elif choice == "knife" and knife in inventory:
        return knife
    elif choice == "sword" and sword in inventory:
        return sword
    elif choice == 'bomb' and bomb in inventory:
        return bomb

# Skriver ut status | player HP & vilket rum man är i


def printPlayerState(currentRoom: Room):
    print("\n---------------")
    print("Player HP: " + str(player.getHealth()) + " ♥")
    print("Location: " + currentRoom.getName())
    print("('I' for Inventory)")

# Skriver ut fight status | enemy HP och player HP och vad i inventroy man kan använda


def printFightState(fightEnemy: EnemyCharacter, inventory):
    print("\n===========================")
    print(
        f"Fighting {fightEnemy.getName()} | HP: {fightEnemy.getHealth()}")
    print("---------------------------")
    print(f"Player HP: {player.getHealth()} ♥")
    printInventoryChoices(inventory)
    print("---------------------------")

# Skriver ut vilket Item man använder

def printPlayerUseState(currentItem: Item):
    currentItemList = ['fist', 'knife', 'sword', 'bomb']
    if currentItem.getItem() in currentItemList:
        print(
            f"\n- Using {currentItem.getItem()}")

    elif currentItem.getItem() == "toilet":
        print(
            "\n- Using toilet"
        )

# - Skriver ut olika val beroende på rum och om enemy lever eller inte

def printPlayerChoices(currentRoom: Room): 
    checkEnemy = currentRoom.getEnemy()
    rooms = ['Room 1', 'Room 2', 'Room 3', 'Room 4', 'Room 5']
    # Kollar om man är i room1-room4
    if currentRoom.getName() in rooms[:-1] and checkEnemy.getHealth() <= 0:
        print('Choices:| go right | go left | go back |')
        print("---------------")
    # Kollar om man är i room1-room5
    elif currentRoom.getName() in rooms and checkEnemy.getHealth() > 0:
        print(f"Choices:| fight {currentRoom.getEnemyInRoom()} | go back |")
        print("---------------")
    
    elif currentRoom.getName() == "Room 5" and checkEnemy.getHealth() <= 0:
        print('Choices:| go back |')
        print("---------------")
    
    elif currentRoom.getName() == "Bar":
        print("Choices:| go right | go left |")
        print("---------------")

    elif currentRoom.getName() == "Toilet":
        print('Choices:| use toilet | go back |')
        print("---------------")

    elif currentRoom.getName() == "Game Room":
        print('Choices: | play | go back |')

# Skriver ut vilka vapen man kan använda baserat på vad som finns i inventory

def printInventoryChoices(inventory):
    inventoryNames = []
    for i in inventory:
        inventoryNames.append(i.getItem())
    joinedList = " | use ".join(inventoryNames)
    print(f"Choices: | use {joinedList} |")

# Ändrar rum beroende på vart man går (right, left, back)

def getRoomInDirection(currentRoom: Room, direction):

    if direction == "right" and currentRoom.getEnemy().getHealth() <= 0:
        return currentRoom.getRoomToRight()
    elif direction == "left" and currentRoom.getEnemy().getHealth() <= 0:
        return currentRoom.getRoomToLeft()
    elif direction == "back":
        return currentRoom.getRoomToBack()

# Lägger till Item i listan inventory beroende på vilken enemy som dödades

def newItemWhenKilled(enemy, inventory):
    if enemy == 'drunkman' and knife not in inventory:
        inventory.append(knife)
        print("** And picked up knife **")
    elif enemy == 'skeleton' and sword not in inventory:
        inventory.append(sword)
        print("** And picked up sword **")
    elif enemy == 'ninja' and bomb not in inventory:
        inventory.append(bomb)
        print("** And picked up bomb **")


# Kollar om man vill spela igen eller inte när man dör/ return True eller False

def playAgain():
    print("\nYou died :-(")
    playAgain = input("Do you wanna play again? y/n :")
    if playAgain == 'y':
        return True
    else:
        print("Hope to see u again!")
        return False

# Printar ut Inventory vapen/// -- Lägga till mer grejer om vi skapar nya Items??


def showInvetory(items):
    print("\n ___________________________________")
    print("|          ** Inventory **          |")
    print("|-----------------------------------|")
    for weapon in items:
        if weapon.getItem() == 'fist':
            print("| Fist: does damage between 2 - 3   |")
        if weapon.getItem() == 'knife':
            print("| Knife: does damage between 0 - 6  |")
        if weapon.getItem() == 'sword':
            print("| Sword: does damage between 1 - 15 |")
        if weapon.getItem() == 'bomb':
            print("| Bomb: does damage between 6 - 7   |")

    print(" ----------------------------------- ")



fist = Item("fist", 2, 3)
knife = Item("knife", 0, 6)
sword = Item("sword", 1, 15)
bomb = Item("bomb", 6, 7)


player = Character(50)


def fightMode(currentRoom: Room, inventory):
    fightEnemy = currentRoom.getEnemy()
    while fightEnemy.getHealth() > 0 and player.getHealth() > 0:

        printFightState(fightEnemy, inventory)
        command = input("What do you wish to do? ")
        subcommands = command.split(" ")
        if subcommands[0] == "use":
            item = useItem(subcommands[1], inventory)
            if item == None:
                print("You are unable to use " + subcommands[1])
            else:
                printPlayerUseState(item)
                print(f"* You attack for: {item.setDamage()} dmg")
                fightEnemy.takeDamage(item.getDamage())
                if fightEnemy.getHealth() > 0:
                    print(
                        f"* {fightEnemy.getName()} attacks for: {fightEnemy.setDamage()} dmg")
                    player.takeDamage(fightEnemy.getDamage())

    if fightEnemy.getHealth() <= 0:
        print(f"You killed {fightEnemy.getName()}")
        newItemWhenKilled(fightEnemy.getName(), inventory)
        if fightEnemy.getName() == "beholder":
            print("\nWow you actually beat the game that's literally impossible..")


currentRoom = createWorld()
mastermind = MasterMind()
hangman = Hangman()
inventory = [fist]
keepPlaying = True
while keepPlaying:

    if currentRoom.getName() == "Hangman Room":
        alive = hangman.play()
        if alive == True:
            currentRoom = getRoomInDirection(currentRoom, "back")
        else:
            player.setPlayerHealth(0)

    if currentRoom.getName() == "Trap":
        print("\nYou walked into a trap & lost 10 ♥ !!!!")
        player.takeDamage(10)
        currentRoom = getRoomInDirection(currentRoom, "back")

    
    if player.getHealth() <= 0:
        keepPlaying = playAgain()
        if keepPlaying == True:
            currentRoom = createWorld()
            inventory = [fist]
            player = Character(50)
            print("\n** Starts Again **")
        else:
            break

    printPlayerState(currentRoom)
    printPlayerChoices(currentRoom)
    command = input("What do you wish to do? ")
    subcommands = command.split(" ")

    if subcommands[0] == "go":
        newRoom = getRoomInDirection(currentRoom, subcommands[1])
        if newRoom == None:
            print("You are unable to move " + subcommands[1])
        else:
            currentRoom = newRoom

    if subcommands[0] == "use":
        item = useItem(subcommands[1], inventory)
        if item == None:
            print("You are unable to use " + subcommands[1])
        else:
            printPlayerUseState(item)

    if subcommands[0] == 'fight':
        if subcommands[1] != currentRoom.getEnemyInRoom():
            print("You are unable to fight " + subcommands[1])
        else:
            fightMode(currentRoom, inventory)

    if command == "play":
        if currentRoom.getName() == 'Game Room':
            moreHealth = mastermind.play()
            if moreHealth == True:
                print("\nCongrats player gets 50♥ health")
                player.gainHealth(50)
        else:
            print("You are unable to play ")

    if command == 'I':
        showInvetory(inventory)

    if command == fist.whatCanThisBe():
        print("\n!!!!! OMFG !!!!!")
        print("You've unlocked the killing punch")
        fist = Item("fist", 1000, 1000)
        inventory[0] = fist



# Ändra så alla rum heter något istället för häger eller vänster?
