# Write a program that will take user input of (4 digits number) and check whether the number is narcissist number or not.

def pow(a):
    b = 0
    while (a>0):
        a = a//10
        b += 1
    return b

def arm(c):
    n = 0
    s = pow(c)
    if (s == 4):
        while (c > 0):
            m = c % 10
            n = n + m**s
            c = c//10
        return n
    else:
        return("invalid value entered")

c = int(input("enter a 4 digit no."))

print(arm(c))
