---
jupyter:
  colab:
  kernelspec:
    display_name: Python 3
    name: python3
  language_info:
    name: python
  nbformat: 4
  nbformat_minor: 0
---

::: {.cell .code id="y8VOh811A9bE"}
``` python
#@title COMP216 Lab exercise 1.
# Please save this notebook as your name
#
# Please insert your name, student number, course and date
# is the proper spots below.
#
# copyrights Narendra Pershad
#
```
:::

::: {.cell .markdown id="Fq8nbpafpY0U"}
**Name: Narendra\
Sid: 123-456-789\
Course: COMP216-001\
Date: September 5, 2023**

------------------------------------------------------------------------

##Instructions

1.  Complete the exercises as far as you possibly can

2.  Rename the workbook to your first name\

3.  Make sure that the notebook is shareable

4.  Upload a link to the Assessment folder in brightspace\

5.  ## You code must work even if the original variable changes

    If you leave the notebook and/or start working at mid-way in the
    notebook, you will have to execute the first cell again to re-load
    the variable etc.
    ##Questions: \[47.5 Marks\]

-   [Working with Sets](#set)
-   [Working with Tuples](#tuple)
-   [Working with Lists](#list)
-   [Working with Dictionaries](#dict)
-   [Conversions between Collections](#conversion)
-   [Iterate a collection](#iterate)
-   [Using the enumerate function](#enumerate)
:::

::: {.cell .code id="a_L-qS0vKURp"}
``` python
#imports and variables
from random import randint

#the following variable will be used in the rest of the exercise
pm = 'justin pierre james trudeau'
instructor = 'narendra pershad'
harry = "You've gotta ask yourself a question: do I feel lucky? …well, do ya, punk?"
numbers = [randint(5, 10) for _ in range(20)]
```
:::

::: {.cell .markdown id="ZgH9uiTwLPfZ"}
##1. `<a name="set">`{=html}`</a>`{=html}Working with sets \[8 Marks\]
:::

::: {.cell .code id="lHCzPapCLVUH"}
``` python
# - 1 mark
# use the set constructor to create a set (assign the new set to a variable) from the variable 'instructor' and print it

```
:::

::: {.cell .code id="p2MOv9RIMP8H"}
``` python
# - 1 mark
# use the add() method to add 'z' to the above set and print it

```
:::

::: {.cell .code id="p2atpDebMV8v"}
``` python
# - 1 mark
#use the remove() method to take ' ' from the set and print it

```
:::

::: {.cell .code id="Il5HqjcfPD8p"}
``` python
# - 1 mark
# define your own new set (assign the new set to a variable)
# use the intersection() method to find the common elements in both sets and print the result

```
:::

::: {.cell .code id="dtCvDvtFPuaw"}
``` python
# - 1 mark
# use the union() method to find all the elements occuring in both sets and print the result

```
:::

::: {.cell .code id="sRfaBsnvOXEC"}
``` python
# - 1 mark
#use the pop() method remove and return an arbitrary elements of the set and print it

```
:::

::: {.cell .code id="UdKDM8NQ8mPj"}
``` python
# - 1 mark
#use the update() function to add 'x', 'y' and 'z' to the set  and print the result

```
:::

::: {.cell .code id="w3hyOYJNMZ2B"}
``` python
# - 1 mark
#use the len() function to get the number of elements in the set and print the result

```
:::

::: {.cell .markdown id="2oaEJMH7QP8f"}
##2. `<a name="tuple">`{=html}`</a>`{=html}Working with tuples \[6
Marks\] Because a tuple is immutable, methods like add(), remove(),
pop() does not exist for tuples
:::

::: {.cell .code id="WGSZ9yrHRFV_"}
``` python
# - 1 mark
# Use the tuple constructor to create a tuple (assign the new set to a variable) from the variable pm and print it
```
:::

::: {.cell .code id="GTtqEpSJSghH"}
``` python
# - 3 marks
# write the statement to produced the following lines of output

## There are 4 e's in the tuple                   #use the count() method
## You can find a at index 15 of the tuple        #use the index() method
## There are 27 elements in the tuple             #use the len() function


```
:::

::: {.cell .code id="CM_JupCbXjyy"}
``` python
# - 1 mark
# use decomposition to print the first, second and the rest of the elements of your tuple

```
:::

::: {.cell .code id="WC-6oIaBYMoQ"}
``` python
# - 1 mark
# use array-like indexing to print the third and fifth element of your tuple

```
:::

::: {.cell .markdown id="wwfdU9TB440D"}
##3. `<a name="list">`{=html}`</a>`{=html}Working with list \[10 Marks\]
:::

::: {.cell .code id="121JIXl2qXtT"}
``` python
# - 1 mark
# Use the list constructor to create a list  (assign the new set to a variable) from the variable 'harry' using the split() method
# of the string class and print it

```
:::

::: {.cell .code id="lfNTrz6arJWc"}
``` python
# - 4 marks
# use the append() method once to add 'Eastwood' to the end of the  list
# use the insert() method to add 'Clint' at the start of the  list
# use the remove() method to remove 'question' from the list
# use the extend() method to add 'Dirty' and 'Harry' to the end of the list
# print the final list

```
:::

::: {.cell .code id="K-sKKdxPsbW8"}
``` python
# - 2 marks
# use the sort() method to order the  list
# print the list
# use the reverse() method to reverse the list
# print the final list

```
:::

::: {.cell .code id="SZORK7R4tZWj"}
``` python
# - 3 mark
# write the statement to produced the following lines of output

## There are 2 do's in the list
## You can find "ask" at index 9 of the list
## There are 17 elements in the list

```
:::

::: {.cell .markdown id="euby2eba0kWr"}
##4. `<a name="dic">`{=html}`</a>`{=html}Working with dictionary \[4
Marks\]
:::

::: {.cell .code id="_8bhodZDy3QU"}
``` python
#use the following dictionary for your exercises
d = {
    3462: 'Artificial Intelligence',
    3468: 'Software Engineering Technician',
    3469: 'Software Engineering Technology',
    3472: 'Artificial Intelligence (FT)',
    3478: 'Software Engineering Technician (FT)',
    3528: 'Health Informatics Technology (FT)',
    3609: 'Game - Programming',
    3668: 'Health Informatics Technology',
    3679: 'Game - Programming (FT)'}
```
:::

::: {.cell .code id="4tdwer_42A6D"}
``` python
# - 1 mark
# display the dictionary


```
:::

::: {.cell .code id="vwTwWh5j3wmb"}
``` python
# - 1 mark
# use the keys() and values() method to display the keys and values

```
:::

::: {.cell .code id="ExUGyOP--_wM"}
``` python
# - 2 mark
# Use the key-index technique to retrieve the name of program 3462
# Use the get() method to retrieve the name of program 3462
# It there a difference?

```
:::

::: {.cell .markdown id="VOKj50Y3iWXq"}
##5. `<a name="conversion">`{=html}`</a>`{=html}Converting from one
collection to another \[7.5 Marks\] There is free inter-conversions
except for dictionary
:::

::: {.cell .code id="e7tcL28HMuBc"}
``` python
# - 2.5 marks
# Use the constructor to obtain a set from each of the three previous collections
# (parts 2, 3 and 4) and print them.
# Notice the iterator variable the dictionary loop represents only the key

```
:::

::: {.cell .code id="2tnfcAeTjWma"}
``` python
# - 2.5 marks
# Use the constructor to obtain a tuple from each of the three previous collections
# (parts 1, 3 and 4) and print them.
# Again, notice the iterator variable the dictionary loop represents only the key

```
:::

::: {.cell .code id="MTFoztohjmJ0"}
``` python
# - 2.5 marks
# Use the constructor to obtain a list from each of the three previous collections
# (parts 1, 2 and 4) and print them.

```
:::

::: {.cell .markdown id="LE9UmvppKbDg"}
##6. `<a name="iterate">`{=html}`</a>`{=html}Iterating a collection \[4
Marks\] The for-in loop facilates iterating a collection
:::

::: {.cell .code id="z5ABdjvpKufk"}
``` python
# - 4 mark
# Use a for-in loop to print each of the previous collection: set, tuple, list and dict
# Notice the iterator variable the dictionary loop represents only the key

```
:::

::: {.cell .markdown id="nKfxb9CFvqD8"}
##7. `<a name="enumerate">`{=html}`</a>`{=html}Using the enumerate
function \[8 Marks\] This function can enumerate both sequences like
sets, tuples, strings and lists as well as mappings like dictionaries\
The enumerate function returns a collection of tuples.\
Each tuples is a pair comprising of the index and the value.
:::

::: {.cell .code id="hbK7KS7Q2MEd"}
``` python
# - 4 mark
# use the enumerate function to print each collection: set, tuple, list and dict
# You must print both the position and the item in the collection

```
:::

::: {.cell .code id="FjcZLRgMOQDL"}
``` python
# - 4 mark
# Use the items() method of the dict class to enumerate a dictionary
# You must print the position, the key and the value
```
:::
