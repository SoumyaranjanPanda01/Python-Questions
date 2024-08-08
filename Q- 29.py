# Print all the armstrong numbers in the range of 100 to 1000

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

l = []

for i in range(100,1000):
    if (i == arm(i)):
        l.append(i)

print(l)