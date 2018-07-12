# Python 3.6.5
# Use this script tp generate gmails based on the cell phone, user's first name, and Organization

import random
def generateAccount():
    num = input("Cell Number: ")
    name = input("User's first name:")
    organization = input("Enter your organization: ")
    print (num)
    account = name
   #Random integer is created and added based on the number 9 (can be changed to whatever number is in your Area code)
    for x in num:
        if x == "9":
            account += (str(random.randint(0,100)))
    print ("Account: " + account + "."+ organization + "@gmail.com")
generateAccount()
