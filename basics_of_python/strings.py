string = "Vicky Gupta"
num = "7827"
print(string[::-1]) #for reversing the strings in java

print(string[0:6])
print(string[6:])

print(string.upper())
print(string.lower())
print(string.capitalize())

print(string.title())       #capitalize every char after any space
print(string.__contains__("Y")) # tells whether string contains any small string or not.
print(string.count("Vicky"))    # counts the number of occurrences of any particular string


print(num.isdigit())    # for checking if string is containing only the numeric chars or not.
print(num.isalnum())    # for checking if string contains both alphabets and numeric values .
print(num.isnumeric())  # same as isdigit() functions.





# STRINGS ARE IMMUTABLE IN PYTHON.
# whatever functions you are using above for making strings mutable, is in background creating a new string for it.
