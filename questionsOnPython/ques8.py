pswd = input("Enter your password: ")

if len(pswd) < 6: print("Password is too short")
elif len(pswd) < 11: print("Password strength is Medium")
else : print("Password is strong")