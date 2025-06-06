# {} represents empty dictionary in python and this is not empty set.
# empty set is represented as : set() in python.
# so do not get confused in this.

# dictionary contains the key value pairs in python just like represented below.

dict1 = {"name": "Vicky", "age": 20, "gender": "male"}
marks = {"Vicky": 80, "Vicky": 85}
print(dict1.get("age"))
print(marks.get("Vicky"))  # if duplicate keys are present in the dictionary then if user fetches data for it then it will fetch last one  data only as shown in marks dictionary example.

# returns the keys and values present in dictionary.
print(marks.keys())
print(marks.values())
