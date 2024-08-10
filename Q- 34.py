# Print first 25 prime numbers

a = 0
num = 2
while (a <= 25):
    for i in range(2,num):
        if (num%i == 0):
            break
    else:
        print(num)
        a += 1
    num += 1