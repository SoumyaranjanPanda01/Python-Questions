# Write  a program that will tell whether the given number is divisible by 3 & 6.

a = int(input("enter a no."))

if (a%6 == 0):
    print("it is divisible by both 3 and 6")
elif (a%3 == 0):
    print("it is divisible by 3")
else:
    print("it is not divisible by either 3 or 6")