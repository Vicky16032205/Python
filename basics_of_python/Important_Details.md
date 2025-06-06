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
