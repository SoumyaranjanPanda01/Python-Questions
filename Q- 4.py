# Write a program that will give you the sum of digits

a = int(input("enter a no."))
n = abs(a)
c = 0
while(n>0):
    b = n%10
    c = c+b
    n = n//10
print(c)