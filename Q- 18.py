# Write a program that will check whether the number is armstrong number or not.

def pow(a):
    b = 0
    while (a>0):
        a = a//10
        b += 1
    return b

def arm(c):
    n = 0
    s = pow(c)
    while (c >0):
        m = c % 10
        n = n + m**s
        c = c//10
    return n

c = int(input("enter a no."))
if (c == arm(c)):
    print("yes it is an armstrong number")
else:
    print("no it is not an armstrong number")