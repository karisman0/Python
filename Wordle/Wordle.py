import random
import colorama

Words = ["HELLO", "MATH", "BYE", "SURE", "GREEN", "YELLOW", "WHAT", "SUPER", "CRISPY", "CRISP", "WAIL", "SHIP", "BLUE", "ORANGE", "DEVOUR", "MILES", "STICK", "GRASS", "WATER", "ENGINE", "CANDY", "RICH", "POOR", "CORN", "GAME", "WHEAT", "MARK", "STEVEN", "BARBIE", "MOUSE", "PC", "OK", "WE", "LESS", "MORE", "SPACE", "RICE", "CARBS", "PULSE", "NUT", "WINTER", "HEALTH", "LIFE", "RAD", "CLASS", "SICK", "MAGIC", "BLACK", "WHITE", "DEATH", "PLAQUE", "QUEST", "FOOD", "QUOTE", "DEVIL", "GOD", "JESUS", "BIBLE", "EAT", "ATTACK", "BIGMAC", "LONG", "SHORT"]
RWord = Words[random.randint(0, len(Words))]
RWord = str(RWord).lower()
AttemptCount = 1
print("-Wordle-")
print("Type the word in lower case")
print("Guess the 2-6 lettered word")
while True:
    Attempt = input("Guess: ")
    if Attempt == RWord:
        print("You got it in " + str(AttemptCount) + " attempts!")
        exit()
    elif Attempt == "IGIVEUP":
        print("You gave up :/ it was " + RWord)
        exit()
    else:
        AttemptCount += 1
        prword = []
        for i in range(0, len(Attempt), 1):
            try:
                if Attempt[i] == RWord[i]:
                    prword.append(colorama.Fore.GREEN + str(Attempt[i]) + colorama.Fore.WHITE)
                elif Attempt[i] in RWord:
                    prword.append(colorama.Fore.YELLOW + str(Attempt[i]) + colorama.Fore.WHITE)
                else:
                    prword.append(colorama.Fore.WHITE + str(Attempt[i]) + colorama.Fore.WHITE)
            except IndexError:
                if len(Attempt) > 6:
                    for x in range(0,len(prword),1):
                        try:
                            prword.pop(0)
                        except:
                            pass
                    prword.append("Word was too long")
                elif Attempt[i] in RWord:
                    prword.append(colorama.Fore.YELLOW + str(Attempt[i]) + colorama.Fore.WHITE)
                else:
                    prword.append(colorama.Fore.WHITE + str(Attempt[i]) + colorama.Fore.WHITE)
    print(*prword)