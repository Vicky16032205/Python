num = int(input("Enter a number: "))

for i in range(1, 11):
    if i == 5:
        print("Skipped 5")
        continue
    print(num, "x" , i, "=" , num*i)