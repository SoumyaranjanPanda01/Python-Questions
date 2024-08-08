# Write a program to find the simple interest when the value of principle,rate of interest and time period is given.

p = int(input("enter the principal amount"))
r = int(input("enter the rate of interest"))
t = int(input("enter the time period"))

m = p/100
n = m*r
ans = n*t

print("your desired profit would be", ans)