sam=int(input("Enter the number:"))
temp=sam
rev=0
while(sam>0):
    dig=sam%10
    rev=rev*10+dig
    sam=sam//10
if(temp==rev):
    print("The number is a palindrome!")
else:
    print("The number isn't a palindrome!")