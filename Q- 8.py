# Write a program to find the euclidean distance between two coordinates.
# Euclidean Distance Theorem = [(p1-q1)^2 + (p2-q2)^2]^1/2

import random

a = random.sample(list(range(10)),2)
b = random.sample(list(range(10)),2)

print(a)
print(b)

x = a[0] - b[0]
y = a[1] - b[1]

m = x**2
n = y**2

s = m+n

import math
ans = math.sqrt(s)
t = format(ans,".2f")

print(t)