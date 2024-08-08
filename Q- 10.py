# Write a program that will take user input of cost price and selling price and determines whether its a loss or a profit

a = int(input("enter cost price"))
b = int(input("enter sellling price"))

c = a-b

if (c >= 0):
    print("you are in loss")
else:
    print("you are in profit")