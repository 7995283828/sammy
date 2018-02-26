s=[]
sam=int(input("Enter number of elements:"))
for i in range(1,sam+1):
    c=int(input("Enter element:"))
    s.append(c)
s.sort()
print("Largest element is:",s[sam-1])