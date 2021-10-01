from character import Character
import random

class Poker:

    def __init__(self, coins):
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

    def printingWelcome(self):
        print("\n=====================")
        print("   Black Jack Room   ")
        print("=====================")

    def printCards(self, dealerHand, playerHand):
        print(f'\n\nDealers hand:{" | ".join(["", *dealerHand, ""])}\n')
        print(f'Players hand:{" | ".join(["", *playerHand, ""])}\n')

    def getCardsValueList(self, cards):
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
            value[1] = value[0] + 11
            value[0] += 1

        elif ess == 2:
            value[1] = value[0] + 12
            value[0] += 2

        elif ess == 3:
            value[1] = value[0] + 13
            value[0] += 3

        elif ess == 4:
            value[1] = value[0] + 14
            value[0] += 4
            

        return value[:2]

    def getFinalValue(self, cardsList):
        bestValue = 0
        for i in cardsList:
            if i <= 21 and i > bestValue: 
                bestValue = i
            elif bestValue == 0:
                bestValue = i

        return bestValue

    def checkWinner(self, valuePlayer, valueDealer):
        
        if valuePlayer > 21:
            return False
        
        elif valueDealer > 21:
            return True

        elif valuePlayer == valueDealer:
            return None

        elif valuePlayer > valueDealer:
            return True

        elif valueDealer > valuePlayer:
            return False

    def playingRound(self, deck):
    
        playerHand = []
        dealerHand = []
        
        playerHand.append(self.dealOneCard(deck))
        playerHand.append(self.dealOneCard(deck))
        dealerHand.append(self.dealOneCard(deck))

        #Kollar om första handen är black jack!
        if self.getFinalValue(self.getCardsValueList(playerHand)) == 21:
                #Om man har black jack får även dealer ett till kort
                dealerHand.append(self.dealOneCard(deck))
                #printar ut korten igen för att se ifall även dealer fått 21
                self.printCards(dealerHand, playerHand)
                #Om dealer in fått black jack så vinner man
                if self.getFinalValue(self.getCardsValueList(dealerHand)) != 21:
                    print("BLACK JACK!!")
                    return True
                #om dealer också fårr black jack så blir det lika
                else:
                    print("Amazing!! Two blackjacks!!!")
                    return None

        else:
            self.printCards(dealerHand, playerHand)
            # Så länge man är under 21 får player välja HIT / STAND
            while self.getFinalValue(self.getCardsValueList(playerHand)) < 21:
                again = input("-------------------\nhit or stand? ")
                if again == "hit":
                    playerHand.append(self.dealOneCard(deck))
                    self.printCards(dealerHand, playerHand)
                elif again == "stand":
                    break
                else:
                    print(f"\nI don't understand what '{again}' means.")
            
            if self.getFinalValue(self.getCardsValueList(playerHand)) > 21:
                dealerHand.append(self.dealOneCard(deck))
                self.printCards(dealerHand, playerHand)
                return False

            while self.getFinalValue(self.getCardsValueList(dealerHand)) < 17:
                dealerHand.append(self.dealOneCard(deck))
                self.printCards(dealerHand, playerHand)
            
            p_checkWinner = self.getFinalValue(self.getCardsValueList(playerHand))
            d_checkWinner = self.getFinalValue(self.getCardsValueList(dealerHand))
            return self.checkWinner(p_checkWinner,d_checkWinner)

    def play(self):
        coins = self.coins
        
        while True:
            # - Skapar kortlek
            deck = self.buildDeck()
            # - Blandar kortlek
            self.shuffle(deck)
            # - Skriver ut Välkommen text
            self.printingWelcome()
            # - Skriver ut player coins
            print(f"Player coins: | {coins} |")
            # - Om man vill spela eller avsluta
            startPlaying = input("\nplay or quit? : ")
            if startPlaying == "play":
                bet = int(input("- Place bet : "))
                if bet == 0:
                    print("*You have to bet atleast 1 coin.")

                elif bet <= coins and bet > 0:
                    winner = self.playingRound(deck)  # Return True or False
                    if winner == True:
                        print("You win!")
                        coins += bet
                    elif winner == None:
                        print("TIE!")
                        continue
                    else:
                        print("You lose!")
                        coins -= bet

                else:
                    print("*You don't have that amount.")

            elif startPlaying == "quit":
                break

            else:
                print(f"\nI don't understand what '{startPlaying}' means.")

        print("\nHope to see you again!")
