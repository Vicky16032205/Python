## == v/s is 

(is) keyword is used in python for finding whether variables are having
     the same memory reference or not whereas the

(==) operator tells you whether both values are the same or not.

- for example:

```
        say we use two variables (m) and (n):
            m = [1,2,3,4] and
            n = m[:] #slicing is being done here, this commands create a copy
                      of m, both are representing the same values but there is created another memory reference.

            so if we do say (m == n) it will say true but if we say (m is n) then it will return false.
```

- so basically what I am trying to say is that the (==) operator will check if values are equal or not.
- but (is) will tell you that the values in memory represent the same allocation or not.

again take another example say

```
        say we use two variables (l1) and (l2):
            l1 = [1,2,3,4] and
            l2 = m #here both are accessing the same memory allocation

            so if we do say (l1 == l2) it will say true but if we say (l1 is l2) then it will return true here.
```

both are representing the same values, but memory allocation being done is not being done same in every case.

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------
## Confusing syntaxes in python

- In this section we will check some python operations where wordings or syntax are changed, but the meaning is the same for both.
- These are some of the syntax asked in interviews.

```
    For example;
            (1 < 2 < 3) this is same as ( (1 < 2) and (2 < 3) )  this will return false.
    Also;
            (1 == 2 < 3) this is same as ( (1 == 2) and (2 < 3) )  this will also return false.
```
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------

## Decimal precision in python does not work well.
```
for example ( (0.1 + 0.1 + 0.1) - 0.3) will always give 0.0 but it does not works like this in python, it will give some value for it which is not correct.
        
        so for this purpose we import library called DECIMAL LIBRARY.
        we need to import this library:
        
                from decimal import Decimal
                (decimal('0.1') + decimal('0.1') + decimal('0.1') - decimal('0.3'))  now this will return decimal('0.0').
```
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# join and split operations

- join and split operations are used to convert string to list and list to string respectively.
- for example,
```
               chai = ["Adrak", "Masala", "Neembu", "simple"]
               print(chai.join("-")) # this will join these words present in the list by giving space as a separator.
```
- so basically join is used to join the list into a string.


```
               word = "My name is Vicky Kumar Gupta"
               print(word.split(" "))   # this will split the word into two parts as there are 5 spaces in between them.
```

- it will print: ['My', 'name', 'is', 'Vicky', 'Kumar', 'Gupta']
- so basically split is used to split the string into a list.


---------------------------------------------------------------------------------------------------------------------------------------------------------------------------
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------


# Splitting problems in python

- In python, if we were working on a directory and wanted to print or use the path of the directory, we would not be able to do so.
- Why? It is because '/' is a special character in python and the directory path is also having '/' in its path, and this will create the problem.
- Python interpreter would not understand what we are trying to do.
- So, we need to use the r'/' to tell the interpreter that we are using a raw string.
```
     - r stands for raw.
     - r is used to tell the interpreter that we are using a raw string so that it will not interpret the special characters.
```

- for example:
```
          chai = "C:\user\pwd\contains" is one path(let's say)
          so when you will try to print it, will recieve error like:
                     File "<python-input-18>", line 1
                     chai = "C:\user\pwd\contains"
                            ^^^^^^^^^^^^^^^^^^^^^^
                     SyntaxError: (unicode error) 'unicodeescape' codec can't decode bytes in position 2-3: truncated \uXXXX escape
                     
          
          So to tackle this error we use r"" string format.
          Syntax is basically same but just add r character in the starting.
          
          chai = r"C:\user\pwd\contains"
          Now if you try to print, it will be printed as it is as written.
```

we can print the same path without using r'/ ' format.
```
          This is done by adding two '\\'
          chai = "C:\\user\\pwd\\contains"
          Now this will print same like the (r) was printing.
          print(chai) will print C:\user\pwd\contains
```
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Python List Comprehension

- In this section we will check some python operations where wordings or syntax are changed, but the meaning is the same for both.
- These are some of the syntax asked in interviews.
for example, Operation for squaring or cubing of number while their initialization can be done in one line.
```
          squared_nums = [x**2 for x in range(0,10)]
          print(squared_nums)
          this will print [0,1,4,9,16,25,36,49,64,81] #which is square of numbers starting from 0 till 9.
          
          In this manner without writing some extra lines, we had achieved our goal of squaring a list containing numbers.
```