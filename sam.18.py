sammy = int(input("Enter lower range: "))
sam = int(input("Enter upper range: "))
for me in range(sammy,sam + 1):
   sum = 0
   temp = me
   while temp > 0:
       digit = temp % 10
       sum += digit ** 3
       temp //= 10

   if me == sum:
       print(me)