import os
import CreatePassword

os.chdir(os.path.dirname(__file__))
if os.path.isfile("pswrd.txt"):
    os.remove("pswrd.txt")
    CreatePassword.newPass()
