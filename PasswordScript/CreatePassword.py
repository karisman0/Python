import os
import random

rndletters = ["LA", "DE", "KA", "HA", "CH", "ML", "KR", "PA", "PY", "PL", "DA"]

os.chdir(os.path.dirname(__file__))

def newPass():
    if not (os.path.isfile("pswrd.txt")):
        pswrd = open("pswrd.txt", "x")

        pswrd = open("pswrd.txt", "w")
        pswrd.write(str(random.randint(0,9)) + "PY" + str(random.randint(0, 2000)) + random.choice(rndletters))

        pswrd = open("pswrd.txt", "r")

newPass()
