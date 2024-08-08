# Write a program to find the volume of the cylinder. Also find the cost ,when the cost of 1litre milk is 40Rs.

r = int(input("enter radius of the cylinder"))
h = int(input("enter height of the cylinder"))

pi = 3.14

m = r**2
v = pi*m*h
p = (v/1000) * 40
c = format(p,".2f")
print("volume of cylinder would be",v,"unit cube and price of that much milk is",c,"ruppees")