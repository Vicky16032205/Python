animal = input("What type of pet do you have? ")
age = int(input("Enter age of the pet: "))

def food(year, breed):
    if year < 2:
        print(f"Give small {breed} food.")
    elif year < 7:
        print(f"Give adult {breed} food.")
    else:
        print(f"Senior {breed} food.")

food(age, animal)