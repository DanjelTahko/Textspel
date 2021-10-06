from room import Room
from item import Item
from character import Character
from enemyCharacter import EnemyCharacter
import shop

# Skriver ut välkomstmeddelande
def welcome():
    print(" _________________________________________________________")
    print("|                                                          |")
    print("|   ___    _   _   _   _    ___    _____    ___    _   _   |")
    print("|  |   \  | | | | |  \| |  / __|  |  __/   / _ \  |  \| |  |")
    print("|  | |\ | | | | | |   \ | | | __  |  \_   | | | | |   \ |  |")
    print("|  | |/ | | \_/ | | |\  | | |_\ | |  /__  | |_| | | |\  |  |")
    print("|  |___/   \___/  |_| \_|  \____/ |_____\  \___/  |_| \_|  |")
    print("|             ____      __   _       _   _____             |")
    print("|            |  _  \   |  |  \ \   / /  |  __/             |")
    print("|            | | \  |  |  |   \ \ / /   |  \_              |") 
    print("|            | |_/  |  |  |    \   /    |  /__             |") 
    print("|            |_____/   |__|     \_/     |_____\            |")
    print("|                                                          |")
    print("|----------------------------------------------------------|")
    print("|                          Made by                         |")
    print("|                   * Daniel & Jonatan *                   |")
    print("|                                                          |")
    print("|                   'new game' to begin                    |")
    print("|                                                          |")
    print("|                  'help' for how to play                  |")
    print("|                  'quit' to quit program                  |")
    print(" ---------------------------------------------------------")

# Skriver ut status | player HP & vilket rum man är i
def printPlayerState(currentRoom: Room, player: Character):
    print("\n-------------------------------")
    print(f"Location: {currentRoom.getName()}")
    print(f"Health: {player.getHealth()} ♥")
    print(f"Coins: {player.getCoins()} ")

# Skriver ut olika val beroende på rum och om enemy lever eller inte
def printRoomChoices(currentRoom: Room): 
    
    # Kollar om man är i room1-room5
    if currentRoom.getEnemy().getHealth() > 0:
        print(f"\nA {currentRoom.getEnemyInRoomName()} wants to fight with you")
        
    elif currentRoom.getName() == "Room 5" and currentRoom.getEnemy().getHealth() <= 0:
        print("\nThis is the last room, congratz you've killed everyone!")
         
    elif currentRoom.getName() == "Shop":
        print('\nYou went into the store ')
        
    elif currentRoom.getName() == "Game Room" or currentRoom.getName() == "Black Jack Room":
        print('\nYou can play and win more coins')

    print("-------------------------------")

# Skriver ut hur man spelar spelet (endast under startsidan)
def printHelp():
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

# Skriver ut vilka val man har baserat på rum. Ifall man inte vet vad man ska göra
def printHelpChoices(currentRoom: Room, fighting):
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
        print("| * 'quit' to end game      |")
        print(" --------------------------- ")
    
    elif currentRoom.getName() in rooms and checkEnemy.getHealth() > 0 and fighting == False:
        print("\n --------------------------- ")
        print("|   Help: Player Choices    |")
        print(" --------------------------- ")
        print("| * Fight                   |")
        print("| * Go back                 |")
        print("| * Use + item in inventory |")
        print("| * 'I' to see inventory    |")
        print("| * 'quit' to end game      |")
        print(" --------------------------- ")

    elif currentRoom.getName() == "Room 5" and checkEnemy.getHealth() <= 0:
        print("\n --------------------------- ")
        print("|   Help: Player choices    |")
        print(" --------------------------- ")
        print("| * Go back                 |")
        print("| * Use + item in inventory |")
        print("| * 'I' to see inventory    |")
        print("| * 'quit' to end game      |")
        print(" --------------------------- ")

    elif currentRoom.getName() == "Bar":
        print("\n --------------------------- ")
        print("|   Help: Player Choices    |")
        print(" --------------------------- ")
        print("| * Go right                |")
        print("| * Go left                 |")
        print("| * Use + item in inventory |")
        print("| * 'I' to see inventory    |")
        print("| * 'quit' to end game      |")
        print(" --------------------------- ")

    elif currentRoom.getName() == "Shop":
        print("\n --------------------------- ")
        print("|   Help: Player Choices    |")
        print(" --------------------------- ")
        print("| * Shop                    |")
        print("| * Go back                 |")
        print("| * Use + item in inventory |")
        print("| * 'I' to see inventory    |")
        print("| * 'quit' to end game      |")
        print(" --------------------------- ")

    elif currentRoom.getName() == "Game Room" or currentRoom.getName() == "Black Jack Room":
        print("\n --------------------------- ")
        print("|   Help: Player Choices    |")
        print(" --------------------------- ")
        print("| * Play to start game      |")
        print("| * Go back                 |")
        print("| * Use + item in inventory |")
        print("| * 'I' to see inventory    |")
        print("| * 'quit' to end game      |")
        print(" --------------------------- ")

    elif fighting == True:
        print("\n --------------------------- ")
        print("|   Help: Player Choices    |")
        print(" --------------------------- ")
        print("| * Use + item in inventory |")
        print("| * 'I' to see inventory    |")
        print(" --------------------------- ")

# Skriver ut Inventory vapen (och potions ifall man har några)
def printInvetory(items):
    print("\n ---------------------------------------")
    print("             ** Inventory **           ")
    print(" --------------------------------------- ")
    for weapon in items:
        if weapon.getItem() == 'fist':
            print("\n| Fist | : does damage between 2 - 3    ")
        if weapon.getItem() == 'knife':
            print("\n| Knife | : does damage between 0 - 6   ")
        if weapon.getItem() == 'spear':
            print("\n| Spear | : does damage between 1 - 8   ")
        if weapon.getItem() == 'axe':
            print("\n| Axe | : does damage between 1 - 10    ")
        if weapon.getItem() == 'sword':
            print("\n| Sword | : does damage between 3 - 15  ")
        if weapon.getItem() == 'bomb':
            print("\n| Bomb | : does damage between 6 - 7    ")
    print("\n --------------------------------------- ")

    checkList=[] 
    for potion in items:
        amount = items.count(potion)
        if potion.getItem() == 'small health' and 'small health' not in checkList:
            print(f"\n| {amount}x | Small health potion: heals 25 HP   ")
            checkList.append('small health')           
        if potion.getItem() == 'large health' and 'large health' not in checkList:
            print(f"\n| {amount}x | Large health potion: heals 50 HP   ")
            checkList.append('large health')
        if potion.getItem() == 'critical hit' and 'critical hit' not in checkList:
            print(f"\n| {amount}x | Critical hit potion: critic hits   ")
            checkList.append('critical hit')
        if potion.getItem() == 'killer punch' and 'killer punch' not in checkList:
            print(f"\n| {amount}x | Killer punch potion: instant kill ")
            checkList.append('killer punch')
    if len(checkList) > 0:
        print("\n --------------------------------------- ")

# Skriver ut vilket Item man använder
def printPlayerUsing(currentItem: Item, player:Character, inventory):
    
    if currentItem.getItem() in shop.getItemsFromInventory(inventory):

        if currentItem.getItem() == "small health":
            print("\n- Drinking small health potion")
            print("* Gains 25 ♥")
            player.gainHealth(25)
            inventory.remove(currentItem)

        elif currentItem.getItem() == "large health":
            print("\n- Drinking large health potion")
            print("* Gains 50 ♥")
            player.gainHealth(50)
            inventory.remove(currentItem)

        elif currentItem.getItem() == "critical hit":
            print("\n- Drinking critical hit potion")
            player.setCriticalDamage()
            inventory.remove(currentItem)

        elif currentItem.getItem() == "killer punch":
            print("\n- Drinking killer punch potion")
            print("You've unlocked the killer punch")
            inventory.remove(currentItem)
            fist = Item("fist", 1000, 1000)
            inventory[0] = fist

        else:
            print(
            f"\n- Using {currentItem.getItem()}")

# Skriver ut status under fight | player och enemy HP
def printFightState(fightEnemy: EnemyCharacter,player:Character):
    print("\n===========================")
    print(
        f"Fighting {fightEnemy.getName()} | HP: {fightEnemy.getHealth()}")
    print("---------------------------")
    print(f"Your HP: {player.getHealth()} ♥")
    print("---------------------------")

# Skriver ut vad man får när man dödat någon
def printWhenEnemyKilled(enemy, player:Character):
    if enemy == 'drunkman':
        player.addCoins(10)
        print("** And picked up 10 coins **")
    elif enemy == 'skeleton':
        player.addCoins(20)
        print("** And picked up 20 coins **")
    elif enemy == 'ninja':
        player.addCoins(30)
        print("** And picked up 30 coins **")
    elif enemy == 'beholder':
        player.addCoins(1000000)
        print('** And picked up a million coins **')
