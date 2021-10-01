
from character import Character
from item import Item


def mainMenu():
    print("\n -------------------- ")
    print("|    *\Shop Menu/*   |")
    print("|--------------------|")
    print("| 1. Weapons         |")
    print("| 2. Potions         |")
    print("| 3. Health          |")
    print("|--------------------|")
    print("| 4. Quit            |") 
    print(" -------------------- ") 

def weaponMenu():
    print("\n ----------------------------------------------------- ")
    print("|                     *\Weapons/*                     |")
    print("|-----------------------------------------------------|")
    print("| 1. Knife  |  Deals damage between 0 - 6  | Cost: 10 |")
    print("| 2. Spear  |  Deals damage between 1 - 8  | Cost: 15 |")
    print("| 3. Axe    |  Deals damage between 1 - 10 | Cost: 20 |")
    print("| 4. Sword  |  Delas damage between 3 - 15 | Cost: 50 |")
    print("| 5. Bombs  |  Deals damage between 6 - 7  | Cost: 50 |") 
    print("|-----------------------------------------------------|")
    print("| 6. Back                                             |") 
    print(" ----------------------------------------------------- ") 

def potionMenu():
    print("\n ------------------------------------------------------------------ ")
    print("|                            *\Potions/*                           |")
    print("|------------------------------------------------------------------|")
    print("| 1. Small Health  | Heals 25 HP                      | Cost: 10   |")
    print("| 2. Large Health  | Heals 50 HP                      | Cost: 15   |")
    print("| 3. Critical Hit  | Critical hit until enemy is dead | Cost: 20   |")
    print("| 4. Killing Punch | Next attack deals 1000 dmg       | Cost: 1000 |") 
    print("|------------------------------------------------------------------|")
    print("| 5. Back                                                          |") 
    print(" ------------------------------------------------------------------ ") 

def getItemsFromInventory(inventory):
    inventoryStrings = []
    for i in inventory:
        inventoryStrings.append(i.getItem())
    return inventoryStrings

def inStore(player: Character):
    while True:
        coins = player.getCoins()
        inventory = player.getInventory()
        mainMenu()
        menuChoice = input("Select menu option: ")
        if menuChoice.isdigit() and int(menuChoice) == 1:
            while True:
                weaponMenu()
                print(f"Your coins: {player.getCoins()}")
                weaponChoice = input("Select menu option: ")

                if weaponChoice.isdigit() and int(weaponChoice) == 1 and coins >= 10 and "knife" not in getItemsFromInventory(inventory):
                    print("* Added knife to inventory") #(coins -= 10) IF not in inventory
                    player.addToInventory(knife)
                    player.loseCoins(10)

                elif weaponChoice.isdigit() and int(weaponChoice) == 2 and coins >= 15 and "spear" not in getItemsFromInventory(inventory):
                    print("* Added spear to inventory") # (coins -= 15)
                    player.addToInventory(spear)
                    player.loseCoins(15)

                elif weaponChoice.isdigit() and int(weaponChoice) == 3 and coins >= 20 and "axe" not in getItemsFromInventory(inventory):
                    print("* Added axe to inventory") # (coins -= 20)
                    player.addToInventory(axe)
                    player.loseCoins(20)

                elif weaponChoice.isdigit() and int(weaponChoice) == 4 and coins >= 50 and "sword" not in getItemsFromInventory(inventory):
                    print("* Added sword to inventory") # (coins -= 50)
                    player.addToInventory(sword)
                    player.loseCoins(50)

                elif weaponChoice.isdigit() and int(weaponChoice) == 5 and coins >= 50 and "bomb" not in getItemsFromInventory(inventory):
                    print("* Added bomb to inventory") # (coins -= 50)
                    player.addToInventory(bomb)
                    player.loseCoins(50)

                elif weaponChoice.isdigit() and int(weaponChoice) == 6:
                    break
                else:
                    print("Not valid choice")
        
        elif menuChoice.isdigit() and int(menuChoice) == 2:
            while True:
                potionMenu()
                print(f"Your coins: {coins}")
                potionChoice = input("Select menu option: ")
                if potionChoice.isdigit() and int(potionChoice) == 1 and coins >=10 :
                    print("* Added small health potion to inventory") # (coins -= 10)
                elif potionChoice.isdigit() and int(potionChoice) == 2 and coins >= 15:
                    print("* Added large health potion to inventory") # (coins -= 15)
                elif potionChoice.isdigit() and int(potionChoice) == 3 and coins >= 20:
                    print("* Added critical hit potion to inventory") # (coins -= 20)
                elif potionChoice.isdigit() and int(potionChoice) == 4 and coins >= 1000:
                    print("* Added killing punch potion to inventory") # (coins -= 1000)
                elif potionChoice.isdigit() and int(potionChoice) == 5:
                    break
                else:
                    print("Not valid choice")

#Weapons
knife = Item("knife", 0, 6)
spear = Item("spear", 1, 8)
axe = Item("axe", 1, 10)
sword = Item("sword", 3, 15)
bomb = Item("bomb", 6, 7)

#Potions

# Add to game!
# Remove items from main
# Add potions with own Potion class

player = Character(50)
player.addCoins(100)
inStore(player)