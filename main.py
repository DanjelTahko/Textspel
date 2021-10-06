from poker import Poker
from item import Item
from character import Character
from mastermind import MasterMind
from gubee import Hangman
import functionsText as text
import functions as func
import shop


def start():
    currentRoom = func.createWorld()
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
                currentRoom = func.getRoomInDirection(currentRoom, "back")
            else:
                player.setPlayerHealth(0)

        # Om currentRoom är Trap
        if currentRoom.getName() == "Trap":
            print("\nYou walked into a trap & lost 10 ♥ !!!!")
            player.takeDamage(10)
            currentRoom = func.getRoomInDirection(currentRoom, "back")

        # Om player HP är 0 (dvs om man är död!)
        if player.getHealth() <= 0:
            print("You died :-(")
            break

        text.printPlayerState(currentRoom, player)
        text.printRoomChoices(currentRoom)
        
        command = input("What do you wish to do? ").lower()
        subcommands = command.split(" ")

        # Om första ordet i input är 'go'
        if subcommands[0] == "go":
            newRoom = func.getRoomInDirection(currentRoom, subcommands[1])
            if newRoom == None:
                print("You are unable to " + command)
            else:
                currentRoom = newRoom
                print(f"- Enters {currentRoom.getName()}")
                
        # Om första ordet i input är 'use'
        elif subcommands[0] == "use":
            item = func.useItem(subcommands, inventory)
            if item == None:
                print("You are unable to " + command)
            else:
                text.printPlayerUsing(item, player, inventory)
            

        # Om första ordet i input är 'fight'
        elif subcommands[0] == 'fight':
            if currentRoom.getEnemy().getHealth() > 0:
                func.fightMode(currentRoom,player, inventory)
            else:
                print("You are unable to " + command)

        # Om input bara är 'play'
        elif command == "play":
            if currentRoom.getName() == 'Game Room':
                if mastermind.play():
                    print("\nCongrats you won 10 coins")
                    player.addCoins(10)

            elif currentRoom.getName() == "Black Jack Room":
                blackjack.play(player)

            else:
                print("You are unable to play in this room ")

        # Om input bara är 'shop'
        elif command == "shop":
            if currentRoom.getName() == "Shop":
                shop.inStore(player)
                currentRoom = func.getRoomInDirection(currentRoom, "back")
            else:
                print("Unable to shop in this room")

        # Om input bara är 'i'
        elif command == 'i':
            text.printInvetory(inventory)

        # Om input bara är 'help'
        elif command == 'help':
            text.printHelpChoices(currentRoom, False)

        # Om input bara är 'quit'
        elif command == 'quit':
            print("\nEnds game..")
            break
        
        # Om input inte är något av ovan if/elif
        else:
            print(f"*Unable to {command}")

        # - Ett fusk som som atm är kommenterat
        #if command == fist.whatCanThisBe():
        #    print("\n!!!!! OMFG !!!!!")
        #    print("You've unlocked the killing punch")
        #    fist = Item("fist", 1000, 1000)
        #    inventory[0] = fist

# Om main.py är main 
if __name__ == "__main__":
    while True:
        text.welcome()
        beginning = input("-> ")
        if beginning == "new game":
            start()
        if beginning == "help":
            text.printHelp()
        if beginning == "quit":
            break


