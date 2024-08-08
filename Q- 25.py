# Write a program that can multiply 2 numbers provided by the user without using the * operator

def mul(a,b):
    c = b
    ans = a
    while (c>1):
        ans = ans + a
        c = c - 1
    return "multiplication of", a, "and", b, "gives", ans

print(mul(12,11))