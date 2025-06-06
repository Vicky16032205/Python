# tuples are immutable in nature just like strings are.
# we cannot change any index element after specifying the tuple.

tup = (1,2,3,4,5,6)


print(tup.__sizeof__())  #this tells how much space is taken by this tuple in the memory.

print(tup.count(5)) # method used to find the count for a number for how many times it occurs in a tuple.