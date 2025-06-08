size = input("Choose from small, medium and large cup: ")

if size == "Small": coffee = "Small"
elif size == "Medium": coffee = "Medium"
elif size == "Large": coffee = "Large"

extra = input("Wanted \"Extra shot\" of espresso : ")

if extra == "Yes":
    print(f"You got {coffee} cup of coffee with extra shot of espresso")
else:
    print(f"You got {coffee} cup of coffee")