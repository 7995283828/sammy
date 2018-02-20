def power(sam,hike):
    if(hike==1):
        return(sam)
    if(hike!=1):
        return(sam*power(sam,hike-1))
sam=int(input("Enter sam: "))
hike=int(input("Enter hike value: "))
print("Result:",power(sam,hike))