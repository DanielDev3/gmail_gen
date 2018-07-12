# Python 3.6.5

import random
def generateAccount():
    num = input("Cell Number: ")
    name = input("User's first name:")
    organization = input("Enter your organization: ")
    print (num)
    account = name
    for x in num:
        if x == "9":
            account += (str(random.randint(0,100)))
    print ("Account: " + account + "."+ organization + "@gmail.com")
generateAccount()
