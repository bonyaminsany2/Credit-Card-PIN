#Hlao Xiong
#sec 01
#from sys import exit

#ask for input
userInput = input("enter your pin: ")

#Pin is set to 1234
PIN= "1234"

#check if pin is correct
if userInput == PIN:
	print("your pin is correct")
	exit()
else:
	print("wrong pin")

print()

#check for second time if still not correct
userInput = input("enter your pin: ")
if userInput == PIN:
	print("your pin is correct")
	exit()
else:
	print ("incorrect pin")
	
print()

#check third time if still not correct
userInput = input("enter your pin: ")
if userInput == PIN:
	print("your pin is correct")
	exit()
else:
	print("Your bank card is now blocked")
	exit()
