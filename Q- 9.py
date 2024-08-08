# Write a program that take a user input of three angles and will find out whether it can form a triangle or not.

a = int(input("enter angle a"))
b = int(input("enter angle b"))
c = int(input("enter angle c"))

if (a+b+c == 180):
    print("these angles can form a triangle")
else:
    print("thesr angles can't form a triangle")