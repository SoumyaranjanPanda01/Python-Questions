# Write a program that will take three digits from the user and add the square of each digit.

def sq(a):
    square = a**2
    return square

def sq_ad(a,b,c):
    square_addition = sq(a) + sq(b) + sq(c)
    return square_addition

print(sq_ad(5,2,3))