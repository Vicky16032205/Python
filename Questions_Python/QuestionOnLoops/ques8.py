num = int(input("Enter a number: "))

# Handle edge cases
if num <= 1:
    print("Not a prime number")
else:
    flag = False
    # Check divisibility from 2 to square root of num
    upper_limit = int(num ** 0.5) + 1
    for i in range(2, upper_limit):
        if num % i == 0:
            print("Not a prime number")
            flag = True
            break
    if not flag:
        print("Prime number")
