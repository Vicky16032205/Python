grade = int(input("Enter your marks here: "))

if grade>89 | grade<101:
    marks = "A"
elif grade>79 | grade<90:
    marks = "B"
elif grade>69 | grade<80:
    marks = "C"
elif grade>59 | grade<70:
    marks = "D"
else:
    marks = "F"

print(f"Your grade is {marks}")