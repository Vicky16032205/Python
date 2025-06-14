num = int(input("Enter a number: "))
ans = 1
while num>0:
    ans *= num
    num -= 1
print("Factorial is:",ans)
