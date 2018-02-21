s=int(input("Enter the number: "))
a=list(map(int,str(s)))
b=list(map(lambda x:x**3,a))
if(sum(b)==s):
    print("The number is an armstrong number. ")
else:
    print("The number isn't an arsmtrong number. ")