day = input("Enter day : ")
age = int(input("Enter age : "))

ticket_price = 0
if age >= 18:
    ticket_price = 12
else:
    ticket_price = 8
if day == "Wednesday":
    ticket_price -= 2

print("Ticket price is : ",ticket_price)
