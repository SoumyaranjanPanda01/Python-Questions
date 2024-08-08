# Write a program that will tell the number of dogs and chicken are there when the user will provide the value of total heads and legs.

def count_animals(h, l):
    a = 0
    while (l>=2):
        if (l/4 == h):
            return "no. of dogs are", h, "no. of chickens are", a
        else:
            h = h - 1
            a += 1
            l = l - 2
    return "no. of dogs are", h, "no. of chickens are", a

print(count_animals(65,180))

