import random
import time
import os

os.system("cls")

Fword = ["Hel--", "Wh--", "Cra--", "List--", "Lolli---", "Mot---", "Lar--", "Si--", "Ext----", "Ho--", "Eve-----", "Ins---", "Sug--", "Bro--", "Yel---", "Bl---", "Rai----", "Hol---", "Mag----", "Bru---", "Bot---", "Key-----", "Div---", "Wa--", "Ba--", "Gr--", "Met--"]
Sword = ["Hello", "What", "Crazy", "Listen", "Lollipop", "Mother", "Large", "Sick", "Extreme", "Hold", "Everyone", "Insane", "Sugar", "Brown", "Yellow", "Block", "Rainbow", "Hollow", "Magical", "Brutal", "Bottom", "Keyboard", "Diving", "Wall", "Ball", "Grab", "Metal"]

ShopPrice = [6, 8]
WordValue = 1
MoneyLoss = float(1)

Words = 0
Money = 0
IOwords = 0

def shop():
    global Money
    global WordValue
    global MoneyLoss
    wantShop = input("Enter shop? Y/N: ")
    os.system("cls")
    if wantShop == "Y" or wantShop == "y":
        print("Money: " + str(Money))
        print("(1) " + "+1 Word Value " + "(" + str(ShopPrice[0]) + "$)")
        print("(2) " + "10% Less Money Lost " + "(" + str(ShopPrice[1]) + "$)")
        print("(0) " + "Exit")
        askShop = input("Buy: ")
        if askShop == "1" and Money >= ShopPrice[0]:
            Money -= ShopPrice[0]
            WordValue += 1
            ShopPrice[0] *= 2
            os.system("cls")
            shop()
        elif askShop == "1" and Money <= ShopPrice[0]:
            os.system("cls")
            print("Not enough money")
            time.sleep(1)
            os.system("cls")
            shop()
        elif askShop == "2" and Money >= ShopPrice[1]:
            lm = float(MoneyLoss * 10 / 100)
            MoneyLoss -= lm
            Money -= ShopPrice[1]
            ShopPrice[1] *= 2
            os.system("cls")
            shop()
        elif askShop == "2" and Money <= ShopPrice[1]:
            os.system("cls")
            print("Not enough money")
            time.sleep(1)
            os.system("cls")
            shop()
        elif askShop == "0":
            os.system("cls")

while True:

    if Words == (IOwords + 10):
        shop()
        IOwords = Words

    print("Words: " + str(Words))
    print("Money: " + str(Money))
    rwn = random.randrange(0, len(Fword))
    print(Fword[rwn])
    Guess = input(str("Your Guess: "))
    os.system("cls")
    if Guess == str(Sword[rwn]) or Guess == str(Sword[rwn].lower()):
        print("+" + str(WordValue) + " $")
        Money += WordValue
    else:
        print("-" + str(MoneyLoss) + " $")
        if Money > 0:
            Money -= float(MoneyLoss)
    time.sleep(1)
    os.system("cls")
    Words += 1