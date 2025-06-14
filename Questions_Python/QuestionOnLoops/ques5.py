word = input("Enter a word: ")
flag = False
for char in word:
    if word.count(char) == 1:
        print(char)
        flag = True
        break

if not flag:
    print("No unique character")