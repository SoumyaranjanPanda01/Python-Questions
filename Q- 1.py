# User will input (3ages).Find the oldest one

a = abs(int(input("enter your age")))
b = abs(int(input("enter your friend's age")))
c = abs(int(input("enter another friend's age")))

if (a>b and a>c):
    print("a is older")
elif (b>a and b>c):
    print("b is older")
elif (c>a and c>b):
    print("c is older")