

class Hangman():

    def __init__(self, misses=0):
        self.misses = misses

    def isItRight(self, list):
        word = ''
        for c in list:
            word += c
        return word

    def display_misses(self, misses):

        if (misses == 0 or misses == 1):
            print("                 .              \n")
            print("                 |              \n")
            print("              .-\"^\"-.         \n")
            print("             /_....._\\         \n")
            print("         .-\"`         `\"-.    \n")
            print("        (  ooo  ooo  ooo  )     \n")
            print("         '-.,_________,.-'      \n")
            print("              /     \\          \n")
            print("             /   0   \\         \n")
            print("            /  --|--  \\        \n")
            print("           /     |     \\       \n")
            print("          /     / \\     \\     \n")
            print("         /                \\    \n")

        elif (misses == 2):
            print("                 .              \n")
            print("                 |              \n")
            print("              .-\"^\"-.         \n")
            print("             /_....._\\         \n")
            print("         .-\"`         `\"-.    \n")
            print("        (  ooo  ooo  ooo  )     \n")
            print("         '-.,_________,.-'      \n")
            print("              /  0  \\          \n")
            print("             / --|-- \\         \n")
            print("            /    |    \\        \n")
            print("           /    / \\    \\      \n")
            print("          /             \\      \n")
            print("         /               \\     \n")

        elif (misses == 3):
            print("                 .              \n")
            print("                 |              \n")
            print("              .-\"^\"-.         \n")
            print("             /_....._\\         \n")
            print("         .-\"`         `\"-.    \n")
            print("        (  ooo  ooo  ooo  )     \n")
            print("         '-.,_________,.-'      \n")
            print("              /--|--\\          \n")
            print("             /   |   \\         \n")
            print("            /   / \\   \\       \n")
            print("           /           \\       \n")
            print("          /             \\      \n")
            print("         /               \\     \n")

        elif (misses == 3):
            print("                 .              \n")
            print("                 |              \n")
            print("              .-\"^\"-.         \n")
            print("             /_....._\\         \n")
            print("         .-\"`         `\"-.    \n")
            print("        (  ooo  ooo  ooo  )     \n")
            print("         '-.,_________,.-'      \n")
            print("              /--|--\\          \n")
            print("             /   |   \\         \n")
            print("            /   / \\   \\       \n")
            print("           /           \\       \n")
            print("          /             \\      \n")
            print("         /               \\     \n")

        elif (misses == 4):
            print("                 .              \n")
            print("                 |              \n")
            print("              .-\"^\"-.         \n")
            print("             /_....._\\         \n")
            print("         .-\"`         `\"-.    \n")
            print("        (  ooo  ooo  ooo  )     \n")
            print("         '-.,_________,.-'      \n")
            print("              /  |  \\          \n")
            print("             /  / \\  \\        \n")
            print("            /         \\        \n")
            print("           /           \\       \n")
            print("          /             \\      \n")
            print("         /               \\     \n")

        elif (misses == 5):
            print("                 .              \n")
            print("                 |              \n")
            print("              .-\"^\"-.         \n")
            print("             /_....._\\         \n")
            print("         .-\"`         `\"-.    \n")
            print("        (  ooo  ooo  ooo  )     \n")
            print("         '-.,_________,.-'      \n")
            print("              / / \\ \\         \n")
            print("             /       \\         \n")
            print("            /         \\        \n")
            print("           /           \\       \n")
            print("          /             \\      \n")
            print("         /               \\     \n")

        elif (misses == 6):
            print("                 .              \n")
            print("                 |              \n")
            print("              .-\"^\"-.         \n")
            print("             /_....._\\         \n")
            print("         .-\"`         `\"-.    \n")
            print("        (  ooo  ooo  ooo  )     \n")
            print("         '-.,_________,.-'      \n")
            print("              /     \\          \n")
            print("             /       \\         \n")
            print("            /         \\        \n")
            print("           /           \\       \n")
            print("          /             \\      \n")
            print("         /               \\     \n")

    def greet(self):
        print("=========================================\n")
        print("             UFO ABDUCTION\n")
        print("=========================================\n")
        print("OH F*CK, You've been abducted by aliens!!\nGuess the the right word to save yourself \n")

    def play(self):

        self.greet()
        codeword = 'nackademin'

        answer = ['_'] * len(codeword)
        guesses = []
        rightLetter = 0
        misses = 0
        wrong = False

        while (rightLetter < len(codeword) and misses < 6):

            answerString = self.isItRight(answer)

            if wrong == True:
                print("Whops, wrong letter!!")

            print(f'Guess the word : | {answerString} |')

            letter = str(input("Enter letter : "))

            for i in range(0, len(codeword)):
                if letter == codeword[i] and letter != answerString[i]:
                    answer[i] = letter
                    rightLetter += 1
                    guesses.append(letter)
                    wrong = False

            if letter not in codeword:
                misses += 1
                guesses.append(letter)
                wrong = True

            self.display_misses(misses)
            print(guesses)

        if (rightLetter == len(codeword) and misses < 6):
            print(
                f'Right word : {codeword}\nGood, you live to die another day !! :-)')
            return True
        else:
            print(
                f'You got abducted by aliens and died :-( ')
            return False
