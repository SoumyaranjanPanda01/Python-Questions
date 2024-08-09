# Write a program to print all the unique combinations of 1,2,3 and 4

x = []

for i in range(1,5):
    for j in range(1,5):
        for k in range(1,5):
            for l in range(1,5):
                if (i != j and i != k and i != l and j != k and j != l and k != l):
                    a = i*1000 + j*100 + k*10 + l
                    x.append(a)
print(x)