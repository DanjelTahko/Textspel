from poker import Poker
from room import Room
from item import Item
from enemyCharacter import EnemyCharacter
from character import Character
from mastermind import MasterMind
from gubee import Hangman
import random
import shop


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

# Kollar om valet USE finns i inventory och returnar ITEM


def useItem(choice, inventory):
    inventoryString = shop.getItemsFromInventory(inventory)
    if choice in inventoryString:
        index = inventoryString.index(choice)
        return inventory[index]
    

# Skriver ut status | player HP & vilket rum man är i


def printPlayerState(currentRoom: Room, player: Character):
    print("\n--------------------")
    print(f"Location: {currentRoom.getName()}")
    print(f"Player: | HP: {str(player.getHealth())} ♥ | Coins: {player.getCoins()} |")
    print("\n('I' for Inventory)")
    

# Skriver ut fight status | enemy HP och player HP och vad i inventroy man kan använda


def printFightState(fightEnemy: EnemyCharacter,player:Character, inventory):
    print("\n===========================")
    print(
        f"Fighting {fightEnemy.getName()} | HP: {fightEnemy.getHealth()}")
    print("---------------------------")
    print(f"Player HP: {player.getHealth()} ♥")
    printInventoryChoices(inventory)
    print("---------------------------")

# Skriver ut vilket Item man använder

def printPlayerUseState(currentItem: Item, inventory):
    
    if currentItem.getItem() in shop.getItemsFromInventory(inventory):
        print(
            f"\n- Using {currentItem.getItem()}")



# - Skriver ut olika val beroende på rum och om enemy lever eller inte

def printPlayerChoices(currentRoom: Room): 
    checkEnemy = currentRoom.getEnemy()
    rooms = ['Room 1', 'Room 2', 'Room 3', 'Room 4', 'Room 5']
    # Kollar om man är i room1-room4
    if currentRoom.getName() in rooms[:-1] and checkEnemy.getHealth() <= 0:
        print('Choices:| go right | go left | go back |')
        print("--------------------")
    # Kollar om man är i room1-room5
    elif currentRoom.getName() in rooms and checkEnemy.getHealth() > 0:
        print(f"Choices:| fight {currentRoom.getEnemyInRoom()} | go back |")
        print("--------------------")
    
    elif currentRoom.getName() == "Room 5" and checkEnemy.getHealth() <= 0:
        print('Choices:| go back |')
        print("--------------------")
    
    elif currentRoom.getName() == "Bar":
        print("Choices:| go right | go left |")
        print("--------------------")

    elif currentRoom.getName() == "Shop":
        print('Choices:| shop | go back |')
        print("---------------")

    elif currentRoom.getName() == "Game Room" or currentRoom.getName() == "Black Jack Room":
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

def newItemWhenKilled(enemy, player:Character):
    if enemy == 'drunkman':
        player.addCoins(10)
        print("** And picked up 10 coins **")
    elif enemy == 'skeleton':
        player.addCoins(20)
        print("** And picked up 20 coins **")
    elif enemy == 'ninja':
        player.addCoins(30)
        print("** And picked up 30 coins **")


# Printar ut Inventory vapen/// -- Lägga till mer grejer om vi skapar nya Items??

def showInvetory(items):
    print("\n ___________________________________")
    print("|          ** Inventory **          |")
    print("|-----------------------------------|")
    for weapon in items:
        if weapon.getItem() == 'fist':
            print("| Fist: does damage between 2 - 3    |")
        if weapon.getItem() == 'knife':
            print("| Knife: does damage between 0 - 6   |")
        if weapon.getItem() == 'spear':
            print("| Spear: does damage between 1 - 8   |")
        if weapon.getItem() == 'axe':
            print("| Axe: does damage between 1 - 10    |")
        if weapon.getItem() == 'sword':
            print("| Sword: does damage between 3 - 15  |")
        if weapon.getItem() == 'bomb':
            print("| Bomb: does damage between 6 - 7    |")

        # lägg till så den visar hur många man har!
        if weapon.getItem() == 'small health':
            print("| Small health potion: heals 25 HP   |")
        if weapon.getItem() == 'large health':
            print("| Large health potion: heals 50 HP   |")
        if weapon.getItem() == 'critical hit':
            print("| Critical hit potion: critic hits   |")
        if weapon.getItem() == 'large health':
            print("| Killing punch potion: instant kill |")

    print(" ----------------------------------- ")




def fightMode(currentRoom: Room, player: Character, inventory):
    fightEnemy = currentRoom.getEnemy()
    while fightEnemy.getHealth() > 0 and player.getHealth() > 0:

        printFightState(fightEnemy, player, inventory)
        command = input("What do you wish to do? ")
        subcommands = command.split(" ")
        if subcommands[0] == "use":
            item = useItem(subcommands[1], inventory)
            if item == None:
                print("You are unable to use " + subcommands[1])
            else:
                printPlayerUseState(item, inventory)
                print(f"* You attack for: {item.setDamage()} dmg")
                fightEnemy.takeDamage(item.getDamage())
                if fightEnemy.getHealth() > 0:
                    print(
                        f"* {fightEnemy.getName()} attacks for: {fightEnemy.setDamage()} dmg")
                    player.takeDamage(fightEnemy.getDamage())

        elif command == "I":
            showInvetory(inventory)

    if fightEnemy.getHealth() <= 0:
        print(f"You killed {fightEnemy.getName()}")
        newItemWhenKilled(fightEnemy.getName(), player)
        if fightEnemy.getName() == "beholder":
            print("\nWow you actually beat the game that's literally impossible..")

def start():
    currentRoom = createWorld()
    player = Character(50)
    fist = Item("fist", 2, 3)
    player.addToInventory(fist)
    inventory = player.getInventory()
    mastermind = MasterMind()
    hangman = Hangman()
    blackjack = Poker()
        
    while True:

        # Om currentRoom är Hangman
        if currentRoom.getName() == "Hangman Room":
            if hangman.play():
                currentRoom = getRoomInDirection(currentRoom, "back")
            else:
                player.setPlayerHealth(0)

        # Om currentRoom är Trap
        if currentRoom.getName() == "Trap":
            print("\nYou walked into a trap & lost 10 ♥ !!!!")
            player.takeDamage(10)
            currentRoom = getRoomInDirection(currentRoom, "back")

        # Om player HP är 0 (dvs om man är död!)
        if player.getHealth() <= 0:
            print("You died :-(")
            break

        printPlayerState(currentRoom, player)
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
                printPlayerUseState(item, inventory)

        if subcommands[0] == 'fight':
            if subcommands[1] != currentRoom.getEnemyInRoom():
                print("You are unable to fight " + subcommands[1])
            else:
                fightMode(currentRoom,player, inventory)

        if command == "play":
            if currentRoom.getName() == 'Game Room':
                if mastermind.play():
                    print("\nCongrats player gets 10 coins")
                    player.addCoins(10)
            elif currentRoom.getName() == "Black Jack Room":
                blackjack.play(player)

            else:
                print("You are unable to play ")

        if command == "shop":
            if currentRoom.getName() == "Shop":
                shop.inStore(player)
            else:
                print("Unable to shop")

        if command == 'I':
            showInvetory(inventory)

        if command == fist.whatCanThisBe():
            print("\n!!!!! OMFG !!!!!")
            print("You've unlocked the killing punch")
            fist = Item("fist", 1000, 1000)
            inventory[0] = fist

if __name__ == "__main__":
    while True:
        print("\n -------------------------")
        print("|         Made by         |")
        print("|  * Daniel & Jonatans *  |")
        print("|                         |")
        print("|   'new game' to begin   |")
        print(" -------------------------")
        if input("-> ") == "new game":
            start()


# Ändra så alla rum heter något istället för häger eller vänster?
# Ändra så man kan välja saker ut inventory när som helst
# Ändra alla player state osv till YOU
