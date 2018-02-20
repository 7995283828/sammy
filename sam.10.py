sam=int(input("Enter number:"))
count=0
while(sam>0):
    count=count+1
    sam=sam//10
print("The number of digits in the number are:",count)