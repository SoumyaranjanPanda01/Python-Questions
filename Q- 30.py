# The current population of a town is 10000. The population of the town is increasing at the rate of 10% per year.
# You have to write a program to find out the population at the end of each of the last 10 years.
# For eg current population is 10000 so the output should be like this:
# 10th year - 10000
# 9th year - 9000
# 8th year - 8100 and so on

def ten_percent(n):
    ans = n/10
    return ans

population = 10000
l = []
l.append(population)

for i in range(9):
    population = population - ten_percent(population)
    l.append(population)

s = {}
s["10th year"] = l[0]
s["9th year"] = l[1]
s["8th year"] = l[2]
s["7th year"] = l[3]
s["6th year"] = l[4]
s["5th year"] = l[5]
s["4th year"] = l[6]
s["3rd year"] = l[7]
s["2nd year"] = l[8]
s["1st year"] = l[9]

print(s)