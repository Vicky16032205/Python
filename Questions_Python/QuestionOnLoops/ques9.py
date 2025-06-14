items = ["apple", "banana", "orange", "apple", "mango"]

unique_items = set()
flag = False
for item in items:
    if item in unique_items:
        print("Duplicate item found : ",item)
        flag = True
        break
    unique_items.add(item)

if not flag:
    print("No duplicate item found")