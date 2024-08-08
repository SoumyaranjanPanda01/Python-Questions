# Write a program to find the sum of first n numbers, where n will be provided by the user. Eg if the user provides n=10 the output should be 55.

def sum(n):
    a = 0
    while (n>0):
        a = a + n
        n = n - 1
    return a

print(sum(10))
