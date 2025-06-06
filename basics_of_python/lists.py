# keep in mind that you can add as many types of object as you want but to use list operations(some) we need to change it to only one
# type of object.
# Lists are mutable in nature.

l1 = [5,12,"Vicky" , [1,2,3]]
print(l1)

# print(l1[3:4]) #for slicing of lists just like we had done in the Strings.
l1.reverse() #it reverses the list.
print(l1)

l1.remove("Vicky")
print(l1)

l2 = [1,2,3,7,8,9,4,5,6]
l2.sort()
print(l2)

l2.append(78)
print(l2)

l2.extend([45,56,12,23])
print(l2)

l2.sort()
print(l2)