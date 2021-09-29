import random


class Poker:

    def __init__(self, name, coins):
        self.name = name
        self.coins = coins

    def buildDeck(self):

        pokerNumber = ['A', '2', '3', '4', '5', '6',
                       '7', '8', '9', '10', 'Kn', 'Q', 'K']
        pokerColor = ['♥', '♣', '♠', '♦']
        deck = []
        for num in pokerNumber:
            for col in pokerColor:
                card = (num + " " + col)
                deck.append(card)
        return deck

    def shuffle(self, deck):
        deck = random.shuffle(deck)
        return deck

    def dealOneCard(self, deck):
        takeOutCardFromDeck = deck[-1]
        deck.pop()
        return takeOutCardFromDeck

    def cardsString(self, cardsList):
        return (" | ".join(["", *cardsList, ""]))

    def printState(self, computerCards, myCards):
        print(f"\n\nDealers hand:{computerCards}\n")
        print(f"{self.name}'s' hand:{myCards}\n")

    def printingWelcome(self):
        print("\n=================")
        print("Simple Black Jack")
        print("=================")

    def checkCard(self, cards):
        value = [0]

        for card in cards:
            cardValue = card.split()
            if cardValue[0].isdigit():
                value[0] += int(cardValue[0])
            else:
                if cardValue[0] == "Kn" or cardValue[0] == "Q" or cardValue[0] == "K":
                    value[0] += 10

                elif card[0] == "A":
                    value.append("A")

        ess = value.count("A")
        if ess == 1:
            value[0] += 1
            value[1] = value[0] + 11
        elif ess == 2:
            value[0] += 2
            value[1] = value[0] + 12
            value.pop()
        elif ess == 3:
            value[0] += 3
            value[1] = value[0] + 13
            value.pop()
            value.pop()
        elif ess == 4:
            value[0] += 4
            value[1] = value[0] + 14
            value.pop()
            value.pop()
            value.pop()

        return value

    def dealerPlay(self, value):
        for i in value:
            if i < 18:
                return True
            else:
                return False

    def checkWinner(self, valuePlayer, valueComputer, value=False):
        computer = 0
        player = 0

        for i in valuePlayer:
            if i == 21:
                player = 21
            elif i <= 21 and i > player:  # 11 mindre eller lika med 21 och 11 är större än 0
                player = i
            elif player == 0:
                player = i

        for i in valueComputer:
            if i == 21:
                computer = 21
            elif i <= 21 and i > computer:
                computer = i
            elif computer == 0:
                computer = i

        if player == 21:
            print("\n BLACK JACK - YOU WIN")
            return True
        elif computer > 21:
            print("\n YOU WIN")
            return True
        elif computer == 21:
            print("\BLACK JACK - YOU LOSE")
            return True
        elif player > 21:
            print("\nYOU LOSE")
            return True

        elif player > 21 and computer > 21:
            print("\n You both lost but you can get this one")

        elif player == 21 and computer == 21:
            print("Wow both got black jack")

        elif player > computer and value == True:
            print("\n YOU WIN")
            return True
        elif computer > player and value == True:
            print("\YOU LOSE")
            return True
        elif value == True:
            print("\nWOW SAME")
            return True

    def playingRound(self, playerPlayAgain, deck):
        active = True
        myHand = []
        computerHand = []
        while active:
            # kollar om man vill ta ett till kort eller pass
            # Lägg till om man får black jack direkt eller ifall någon är över 21

            # Börjar med två kort
            if len(myHand) < 2:
                myHand.append(self.dealOneCard(deck))
                myHand.append(self.dealOneCard(deck))
                computerHand.append(self.dealOneCard(deck))

            # Skriver ut Dealers hand & Players hand
            self.printState(self.cardsString(computerHand),
                            self.cardsString(myHand))

            # Skriver ut value för korten man har i hand, både player & dealer
            print(
                f"Your value: {self.checkCard(myHand)}, Computer value: {self.checkCard(computerHand)}")
            print("----------------")

            # Kollar om någon har Black Jack eller är över 21 MEEEEN funkar inte helt!! om player har [20, 26] så kommer player förlora
            chek = self.checkWinner(self.checkCard(
                myHand), self.checkCard(computerHand), False)

            # Om någon har black jack eller över 21 så avslutas det
            if chek == True:
                active == False
                break
            
            # Player input | HIT or STAND?
            again = input("hit or stand? ")
            if again == "hit":
                myHand.append(self.dealOneCard(deck))
            elif again == "stand":
                playerPlayAgain = False
            else:
                print(f"\nUnable to choose {again}")

            dealerPlayAgain = self.dealerPlay(self.checkCard(computerHand))
            if dealerPlayAgain == True:
                computerHand.append(self.dealOneCard(deck))

            # Om varken Player eller Dealer tar ett till kort kollar den vem som har högst
            elif dealerPlayAgain == False and playerPlayAgain == False:
                self.checkWinner(self.checkCard(myHand),
                                 self.checkCard(computerHand), True)
                active = False


    def play(self):
        deck = self.buildDeck()
        self.shuffle(deck)

        playerPlayAgain = True
        

        self.printingWelcome()
        self.playingRound(playerPlayAgain, deck)
           

#name = input("Write your name: ")
player = Poker("Daniel", 20)
yesyesyes = True
while yesyesyes:
    player.play()
    againnn = input("Do you wanna play again? y/n")
    if againnn == 'y':
        player.play()
    else:
        print("\nHope to see you again!")
        yesyesyes = False


# 1. bet 
# 2. deal()
# 3. double | hit | stand (endast jag spelar?)
# 4. dealer plays
# 5. play again / leave ?