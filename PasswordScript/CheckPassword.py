import os

os.chdir(os.path.dirname(__file__))
if os.path.isfile("pswrd.txt"):

    pswrd = open("pswrd.txt", "r")

    attempt = input("Password: ")

    if attempt == str(pswrd.read()):
        print("Password Correct!")
    else:
        print("Password Wrong.")
else:
    print("Password Not Created")