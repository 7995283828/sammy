sam = int(input("Enter the Year: "))

if (( sam%400 == 0)or (( sam%4 == 0 ) and ( sam%100 != 0))):
    print("%d is a Leap Year" %sam)
else:
    print("%d is not a Leap Year" %sam)