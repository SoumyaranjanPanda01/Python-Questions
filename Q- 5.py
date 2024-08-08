# Write a program that will reverse a number.Also it checks whether the reverse is true.

a = int(input("enter a no."))
n = abs(a)
b = 0
while(n>0):
     c = n%10
     b = b*10+c
     n = n//10
print(b)
if (b == a):
    print("the reverse is false")
else:
    print("the reverse is true")


    