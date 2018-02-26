def sumOfAP(a, b, c) :
    sum = 0
    x = 0
    while x < c :
        sum = sum + a
        a = a + b
        x = x + 1
    return sum
c =2
a =2
b =2
print (sumOfAP(a, b, c))