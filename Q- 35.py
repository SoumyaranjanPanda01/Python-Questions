# Print the first 20 numbers of a Fibonacci series

def fibonacci():
    a = []
    f = 1
    s = 2
    a.append(f)
    a.append(s)
    for i in range(1,19):
        ans = a[i] + a[i-1]
        a.append(ans)
    return a

print(fibonacci())



