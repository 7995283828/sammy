sam = int(input("How many figures : "))
sammy = []
sami = []
for x in range(1,sam+1):
    s = int(input("Enter value" + str(x) + " : "))
    sammy.append(s)
for m in range(len(sammy)):
    e = min(sammy)
    sammy.remove(e)
    sami.append(e)
h = ' '.join(str(x) for x in sami)
print(h)