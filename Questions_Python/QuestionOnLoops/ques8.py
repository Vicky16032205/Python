num = int(input("Enter a number: "))
flag = False
for i in range(2,num):
    if num%i == 0:
        print("Not a prime number")
        flag = True
        break
if not flag:
    print("Prime number")