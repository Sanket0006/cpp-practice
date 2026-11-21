n = 833
b = 7
new = 0

baseBRep = []


while (n > 0):
    baseBRep.append(n % b)
    n //= b 

newNum = "".join(map(str, baseBRep[::-1]))

print(newNum)