# User will input an integer. Write a program to swap the numbers

a = int(input("enter a no."))
n = abs(a)
b = 0
while(n>0):
     c = n%10
     b = b*10+c
     n = n//10
print(b)