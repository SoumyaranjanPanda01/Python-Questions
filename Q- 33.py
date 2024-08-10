# User will provide 2 numbers you have to find the by LCM of those 2 numbers

n = int(input("enter a no."))
m = int(input("enter a no."))

x =[]
for i in range(1,n+1):
    if(n%i == 0):
        x.append(i)

y = []
for j in range(1,m+1):
    if(m%j == 0):
        y.append(j)

max = 0
for a in x:
    for b in y:
        if (a == b):
            max = a

lcm = (n*m)/max
print(lcm)