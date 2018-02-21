sam = int(input("Enter lower range: "))
sammy = int(input("Enter upper range: "))
for me in range(sam,sammy + 1):
    if me > 1:
       for i in range(2,me):
           if (me % i) == 0:
               break
       else:
           print(me)