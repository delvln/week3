try:
   hours = int(input("Enter Hours: "))
   rate = int(input("Enter Rate: "))
   pay = hours*rate
   if hours < 40:
       print("Pay",pay)
   else:
        if hours >= 40:
            print("Pay",(40*rate) + ((hours%40)*1.5)*10)c
except:
    print("Error, please enter numeric input")

