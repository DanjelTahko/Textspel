import random


class MasterMind():

    def __init__(self, amountOfNumbers=9, length=4):
        self.amountOfNumbers = amountOfNumbers
        self.length = length

    def secretNumber(self):
        code = []
        length = 4
        i = 0
        while i < length:
            if i == 0:
                code.insert(i, random.randint(1, 9))
            elif i == 1:
                code.insert(i, random.randint(0, 8))
            elif i == 2:
                code.insert(i, random.randint(2, 7))
            else:
                code.insert(i, random.randint(0, 9))
            j = 0
            ok = True
            while j < i and ok == True:
                if code[i] == code[j]:
                    ok = False
                else:
                    j += 1
            if ok == False:
                code.pop(i)
            else:
                i += 1
        return code

    def makeGuess(self, secretCode):
        correctGuessLength = False
        while not correctGuessLength:
            guess = []
            try:
                guess = [int(i) for i in str(
                    input("\nGuess the four-digit number: "))]
            except ValueError:
                print("Integers only!")
            if len(guess) == len(secretCode):
                correctGuessLength = True
            else:
                print("Try again! \n")
        return guess

    def checkCode(self, secretCode, guessedCode):
        rightPlace = 0
        evaluateCode = []
        for pos, number in enumerate(guessedCode):
            if number == secretCode[pos]:
                evaluateCode.append(str(number))
                rightPlace += 1
            elif number in secretCode:
                evaluateCode.append("C")
            else:
                evaluateCode.append("-")
        return rightPlace, evaluateCode

    def play(self):
        rightPlace = 0
        secretCode = self.secretNumber()
        rounds = 0
        print(" _________________________________")
        print("|    ** M A S T E R M I N D **    |")
        print("|Guess numbers between 1023 - 9876|")
        print("|     * only unique numbers *     |")
        print(" ---------------------------------")
        while rightPlace < len(secretCode) and rounds <= 4:
            guessedCode = self.makeGuess(secretCode)
            rightPlace, evaluateCode = self.checkCode(secretCode, guessedCode)
            print(f'Right place: {rightPlace}')
            print(evaluateCode)
            rounds += 1
        if rounds >= 4 and rightPlace < len(secretCode):
            print(f'You lost, right number was: {secretCode}')
            return False
        else:

            return True
