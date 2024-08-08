# Write a program that will give you the in hand salary after deduction of HRA(10%),DA(5%),PF(3%),
# and tax(if salary is between 5-10 lakh–10%),(11-20lakh–20%),(20< _   – 30%)(0-5lakh print 0).

def hra(a):
    hra = (a * 10)/100
    return hra

def da(b):
    da = (b * 5)/100
    return da

def pf(c):
    pf = (c * 3)/100
    return pf

def tax(d):
    l = 100000
    if (d > 5*l and d < 10*l):
        tax = (d * 10)/100
    elif (d > 11*l and d < 20*l):
        tax = (d * 20)/100
    elif (d > 20*l):
        tax = (d * 30)/100
    else:
        tax = (d * 0)/100
    return tax

def salary(s):
    a = hra(s)
    b = da(s)
    c = pf(s)
    d = tax(s)
    in_hand_salary = s - (a+b+c+d)
    return "your salary after all deduction is", in_hand_salary

print(salary(10000000))