st = {1,2,3,4,5,6}
print(st)

st2 = {1,1,1,1,1,1,2,7}   # elements occurring more than once will not be counted.
print(st2)

st.add(54)
print(st)

print(st.union(st2))          # this is method for finding the union of two sets as we used to do in our school time.
print(st.intersection(st2))   # this finds us the intersection of two sets.