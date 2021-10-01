
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
    print("| 5. Bomb   |  Deals damage between 6 - 7  | Cost: 50 |") 
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

def inStore(coins):
    while True:
        mainMenu()
        menuChoice = input("Select menu option: ")
        if menuChoice.isdigit() and int(menuChoice) == 1:
            while True:
                weaponMenu()
                print(f"Your coins: {coins}")
                weaponChoice = input("Select menu option: ")
                if weaponChoice.isdigit() and int(weaponChoice) == 1 and coins >= 10:
                    print("* Added knife to inventory") #(coins -= 10) IF not in inventory
                elif weaponChoice.isdigit() and int(weaponChoice) == 2 and coins >= 15:
                    print("* Added spear to inventory") # (coins -= 15)
                elif weaponChoice.isdigit() and int(weaponChoice) == 3 and coins >= 20:
                    print("* Added axe to inventory") # (coins -= 20)
                elif weaponChoice.isdigit() and int(weaponChoice) == 4 and coins >= 50:
                    print("* Added sword to inventory") # (coins -= 50)
                elif weaponChoice.isdigit() and int(weaponChoice) == 5 and coins >= 50:
                    print("* Added bomb to inventory") # (coins -= 50)
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



inStore(50)