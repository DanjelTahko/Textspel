from tacoKlasserTest import Room
from tacoKlasserTest import Item
from tacoKlasserTest import EnemyCharacter
from tacoKlasserTest import Character
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
    toilet = Room("Toilet")
    game = Room("Game Room")
    hangmanRoom = Room("Hangman Room")
    trap = Room("Trap")

    air = EnemyCharacter('Air', 0, 0, 0)
    drunkman = EnemyCharacter('drunkman', 10, 0, 2)
    skeleton = EnemyCharacter('skeleton', 25, 2, 5)
    ninja = EnemyCharacter('ninja', 40, 5, 10)
    beholder = EnemyCharacter('beholder', 1000, 50, 100)

    bar.setRoomtoRight(firstRoom)
    bar.setRoomtoLeft(toilet)  # Vänstar om BAR - Toilet
    bar.setEnemytoRoom(air)  # //// Enemy till BAR - Air
    toilet.setRoomToBack(bar)  # Back om TOILET - Bar

    firstRoom.setRoomtoRight(game)  # Höger om Room 1 - Game Room
    firstRoom.setRoomtoLeft(secondRoom)  # Vänster om Room 1 - Room 2
    firstRoom.setRoomToBack(bar)  # Back om Room 1 - Bar
    firstRoom.setEnemytoRoom(drunkman)  # Enemy to room (Drunkman)
    game.setRoomToBack(firstRoom)  # Back om Game Room - Room 1
    game.setEnemytoRoom(air)  # //// Enemy till Game Room - Air

    secondRoom.setRoomtoLeft(trap)  # ---- trapROOM??
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
    fourthRoom.setEnemytoRoom(EnemyCharacter('skeleton', 25, 2, 5))

    fifthRoom.setRoomToBack(fourthRoom)
    fifthRoom.setEnemytoRoom(beholder)

    hangmanRoom.setRoomToBack(thirdRoom)
    trap.setRoomToBack(toilet)

    return bar

# Kollar om valet USE finns i inventory och returnar ITEM


def useItem(choise, inventory):
    if choise == "fist" and fist in inventory:
        return fist
    elif choise == "knife" and knife in inventory:
        return knife
    elif choise == "sword" and sword in inventory:
        return sword
    elif choise == 'bomb' and bomb in inventory:
        return bomb
    elif choise == "toilet" and currentRoom.getName() == "Toilet":
        return toilet

# Skriver ut status | player HP & vilket rum man är i


def printPlayerState(currentRoom: Room):
    print("\n---------------")
    print("Player HP: " + str(player.getHealth()) + " ♥")
    print("Location: " + currentRoom.getName())
    print("('I' for Inventory)")

# Skriver ut fight status | enemy HP och player HP och vad i inventroy man kan använda


def printFightState(fightEnemy: EnemyCharacter, inventory: list):
    print("\n===========================")
    print(
        f"Fighting {fightEnemy.getName()} | HP: {fightEnemy.getHealth()}")
    print("---------------------------")
    print(f"Player HP: {player.getHealth()} ♥")
    printInventoryChoises(inventory)
    print("---------------------------")

# Skriver ut vilket Item man använder


def printPlayerUseState(currentItem: Item):
    if currentItem.getItem() == "fist":
        print(
            f"\n- Using {currentItem.getItem()}")
    elif currentItem.getItem() == "knife":
        print(
            f"\n- Using {currentItem.getItem()}")
    elif currentItem.getItem() == "sword":
        print(
            f"\n- Using {currentItem.getItem()}")
    elif currentItem.getItem() == "bomb":
        print(
            f"\n- Using {currentItem.getItem()}")
    elif currentItem.getItem() == "toilet":
        print(
            "\n- Using toilet"
        )

# - Skriver ut olika val beroende på rum och om enemy lever eller inte
# Bara fram till rum 2, lägg till rum tre *** Denna borde kunna gå att förenkla??


def printPlayerChoises(currentRoom: Room):
    checkEnemy = currentRoom.getEnemy()
    if currentRoom.getName() == "Bar":
        print("Choises:| go right | go left |")
        print("---------------")
    elif currentRoom.getName() == "Room 1" and checkEnemy.getHealth() <= 0:
        print('Choises:| go right | go left | go back |')
        print("---------------")
    elif currentRoom.getName() == "Room 1" and checkEnemy.getHealth() > 0:
        print(f"Choises:| fight {currentRoom.getEnemyInRoom()} | go back |")
        print("---------------")
    elif currentRoom.getName() == "Room 2" and checkEnemy.getHealth() <= 0:
        print('Choises:| go right | go left | go back |')
        print("---------------")
    elif currentRoom.getName() == "Room 2" and checkEnemy.getHealth() > 0:
        print(
            f'Choises:| fight {currentRoom.getEnemyInRoom()} | go back |')
        print("---------------")

    elif currentRoom.getName() == "Room 3" and checkEnemy.getHealth() <= 0:
        print('Choises:| go right | go left | go back |')
        print("---------------")
    elif currentRoom.getName() == "Room 3" and checkEnemy.getHealth() > 0:
        print(
            f'Choises:| fight {currentRoom.getEnemyInRoom()} | go back |')
        print("---------------")

    elif currentRoom.getName() == "Room 4" and checkEnemy.getHealth() <= 0:
        print('Choises:| go right | go left | go back |')
        print("---------------")
    elif currentRoom.getName() == "Room 4" and checkEnemy.getHealth() > 0:
        print(
            f'Choises:| fight {currentRoom.getEnemyInRoom()} | go back |')
        print("---------------")

    elif currentRoom.getName() == "Room 5" and checkEnemy.getHealth() <= 0:
        print('Choises:| go back |')
        print("---------------")

    elif currentRoom.getName() == "Room 5" and checkEnemy.getHealth() > 0:
        print(
            f'Choises:| fight {currentRoom.getEnemyInRoom()} | go back |')
        print("---------------")

    elif currentRoom.getName() == "Toilet":
        print('Choises:| use toilet | go back |')
        print("---------------")
    elif currentRoom.getName() == "Game Room":
        print('Choises: | play | go back |')

# Skriver ut vilka vapen man kan använda baserat på vad som finns i inventory


def printInventoryChoises(inventory: list):
    count = 0
    for i in range(len(inventory)):
        count += 1
    if count == 1:
        print(f"Choises: | use {inventory[0].getItem()} |")
    elif count == 2:
        print(
            f"Choises: | use {inventory[0].getItem()} | use {inventory[1].getItem()} |")
    elif count == 3:
        print(
            f"Choises: | use {inventory[0].getItem()} | use {inventory[1].getItem()} | use {inventory[2].getItem()} |")
    elif count == 4:
        print(
            f"Choises: | use {inventory[0].getItem()} | use {inventory[1].getItem()} | use {inventory[2].getItem()} | use {inventory[3].getItem()} |")

# Ändrar rum beroende på vart man går (right, left, back)


def getRoomInDirection(currentRoom: Room, direction):

    if direction == "right" and currentRoom.getEnemy().getHealth() <= 0:
        return currentRoom.getRoomToRight()
    elif direction == "left" and currentRoom.getEnemy().getHealth() <= 0:
        return currentRoom.getRoomToLeft()
    elif direction == "back":
        return currentRoom.getRoomToBack()

# Lägger till Item i listan inventory beroende på vilken enemy som dödades


def newItemWhenKilled(enemy, inventory: list):
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


def showInvetory(items: list):
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


toilet = Item("toilet", 0, 0)
fist = Item("fist", 2, 3)
knife = Item("knife", 0, 6)
sword = Item("sword", 1, 15)
bomb = Item("bomb", 6, 7)


player = Character(50)


def fightMode(currentRoom: Room, inventory: list):
    fightEnemy = currentRoom.getEnemy()
    while fightEnemy.getHealth() > 0 and player.getHealth() > 0:

        printFightState(fightEnemy, inventory)
        # ändra till siffror eller kanske tom ta bort use?
        command = input("What do you wish to do? ")
        subcommands = command.split(" ")
        if subcommands[0] == "use":
            item = useItem(subcommands[1], inventory)
            if item == None:
                print("You are unable to use " + subcommands[1])
            else:
                printPlayerUseState(item)
                # Kanske ändra nedan till en egen funktion?
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

    # Gör detta till en funktion??
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
    printPlayerChoises(currentRoom)
    command = input("What do you wish to do? ")
    subcommands = command.split(" ")

    # Kanske ändra så att när enemey är död så har den status död?
    # Istället som nu att den kollar currentRoom.enemyhealth < 0
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


# Ändra i mastermind så man ser hur många rounds kvar
# Ändra så man måste skriva bokstäver i hänga gubbe

#Ändra knaske inventory till dictionary
#Lägg till map? som kanske skriver fil så man vet var man är