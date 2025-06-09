age = int(input("Enter your age : "))

if(age<13):
    print("Child")
elif(age>=13 | age <= 19):
    print("Teenagers")
elif(age>=20 | age <= 59):
    print("Adults")
else:
    print("Senior")
