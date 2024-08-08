# Write a program that can find the factorial of a given number provided by the user.

def factorial(n):
    a = 1
    while (n>0):
        a = a*n
        n -= 1
    return a

print(factorial(7))