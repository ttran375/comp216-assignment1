# + id="y8VOh811A9bE"
#@title COMP216 Lab exercise 1.
# Please save this notebook as your name
#
# Please insert your name, student number, course and date
# is the proper spots below.
#
# copyrights Narendra Pershad
#

# + id="a_L-qS0vKURp"
#imports and variables
from random import randint

#the following variable will be used in the rest of the exercise
pm = 'justin pierre james trudeau'
instructor = 'narendra pershad'
harry = "You've gotta ask yourself a question: do I feel lucky? …well, do ya, punk?"
numbers = [randint(5, 10) for _ in range(20)]


# + id="lHCzPapCLVUH"
# - 1 mark
# use the set constructor to create a set (assign the new set to a variable) from the variable 'instructor' and print it
instructor_set = set(instructor)
print(instructor_set)


# + id="p2MOv9RIMP8H"
# - 1 mark
# use the add() method to add 'z' to the above set and print it
instructor_set.add('z')
print(instructor_set)


# + id="p2atpDebMV8v"
# - 1 mark
#use the remove() method to take ' ' from the set and print it
instructor_set.remove(' ')
print(instructor_set)


# + id="Il5HqjcfPD8p"
# - 1 mark
# define your own new set (assign the new set to a variable)
# use the intersection() method to find the common elements in both sets and print the result
new_set = {'a', 'r', 'e', 'd'}
common_elements = instructor_set.intersection(new_set)
print(common_elements)


# + id="dtCvDvtFPuaw"
# - 1 mark
# use the union() method to find all the elements occuring in both sets and print the result
all_elements = instructor_set.union(new_set)
print(all_elements)


# + id="sRfaBsnvOXEC"
# - 1 mark
#use the pop() method remove and return an arbitrary elements of the set and print it
removed_element = instructor_set.pop()
print(removed_element)


# + id="UdKDM8NQ8mPj"
# - 1 mark
#use the update() function to add 'x', 'y' and 'z' to the set  and print the result
instructor_set.update(['x', 'y', 'z'])
print(instructor_set)


# + id="w3hyOYJNMZ2B"
# - 1 mark
#use the len() function to get the number of elements in the set and print the result
set_length = len(instructor_set)
print(set_length)


# + id="WGSZ9yrHRFV_"
# - 1 mark
# Use the tuple constructor to create a tuple (assign the new set to a variable) from the variable pm and print it
pm_tuple = tuple(pm)
print(pm_tuple)


# + id="GTtqEpSJSghH"
# - 3 marks
# write the statement to produced the following lines of output

## There are 4 e's in the tuple                   #use the count() method
## You can find a at index 15 of the tuple        #use the index() method
## There are 27 elements in the tuple             #use the len() function

e_count = pm_tuple.count('e')
a_index = pm_tuple.index('a')
tuple_length = len(pm_tuple)

print(f"There are {e_count} e's in the tuple")
print(f"You can find a at index {a_index} of the tuple")
print(f"There are {tuple_length} elements in the tuple")


# + id="CM_JupCbXjyy"
# - 1 mark
# use decomposition to print the first, second and the rest of the elements of your tuple
first, second, *rest = pm_tuple
print(first)
print(second)
print(rest)


# + id="WC-6oIaBYMoQ"
# - 1 mark
# use array-like indexing to print the third and fifth element of your tuple
print(pm_tuple[2])
print(pm_tuple[4])


# + id="121JIXl2qXtT"
# - 1 mark
# Use the list constructor to create a list  (assign the new set to a variable) from the variable 'harry' using the split() method
# of the string class and print it
harry_list = harry.split()
print(harry_list)


# + id="lfNTrz6arJWc"
# - 4 marks
# use the append() method once to add 'Eastwood' to the end of the  list
# use the insert() method to add 'Clint' at the start of the  list
# use the remove() method to remove 'question' from the list
# use the extend() method to add 'Dirty' and 'Harry' to the end of the list
# print the final list

harry_list.append('Eastwood')
harry_list.insert(0, 'Clint')
harry_list.remove('question:')
harry_list.extend(['Dirty', 'Harry'])
print(harry_list)


# + id="K-sKKdxPsbW8"
# - 2 marks
# use the sort() method to order the  list
# print the list
# use the reverse() method to reverse the list
# print the final list

harry_list.sort()
print(harry_list)
harry_list.reverse()
print(harry_list)


# + id="SZORK7R4tZWj"
# - 3 mark
# write the statement to produced the following lines of output

do_count = harry_list.count('do')
ask_index = harry_list.index('ask')
list_length = len(harry_list)

print(f"There are {do_count} do's in the list")
print(f"You can find 'ask' at index {ask_index} of the list")
print(f"There are {list_length} elements in the list")


# + id="_8bhodZDy3QU"
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


# + id="4tdwer_42A6D"
# - 1 mark
# display the dictionary
print(d)


# + id="vwTwWh5j3wmb"
# - 1 mark
# use the keys() and values() method to display the keys and values
print(d.keys())
print(d.values())


# + id="ExUGyOP--_wM"
# - 2 mark
# Use the key-index technique to retrieve the name of program 3462
# Use the get() method to retrieve the name of program 3462
# It there a difference?

program_3462 = d[3462]
program_3462_get = d.get(3462)

print(program_3462)
print(program_3462_get)


# + id="e7tcL28HMuBc"
# - 2.5 marks
# Use the constructor to obtain a set from each of the three previous collections
# (parts 2, 3 and 4) and print them.
# Notice the iterator variable the dictionary loop represents only the key

tuple_set = set(pm_tuple)
list_set = set(harry_list)
dict_set = set(d)

print(tuple_set)
print(list_set)
print(dict_set)


# + id="2tnfcAeTjWma"
# - 2.5 marks
# Use the constructor to obtain a tuple from each of the three previous collections
# (parts 1, 3 and 4) and print them.
# Again, notice the iterator variable the dictionary loop represents only the key

set_tuple = tuple(instructor_set)
list_tuple = tuple(harry_list)
dict_tuple = tuple(d)

print(set_tuple)
print(list_tuple)
print(dict_tuple)


# + id="MTFoztohjmJ0"
# - 2.5 marks
# Use the constructor to obtain a list from each of the three previous collections
# (parts 1, 2 and 4) and print them.

set_list = list(instructor_set)
tuple_list = list(pm_tuple)
dict_list = list(d)

print(set_list)
print(tuple_list)
print(dict_list)


# + id="z5ABdjvpKufk"
# - 4 mark
# Use a for-in loop to print each of the previous collection: set, tuple, list and dict
# Notice the iterator variable the dictionary loop represents only the key

for item in instructor_set:
    print(item)

for item in pm_tuple:
    print(item)

for item in harry_list:
    print(item)

for key in d:
    print(key)


# + id="hbK7KS7Q2MEd"
# - 4 mark
# use the enumerate function to print each collection: set, tuple, list and dict
# You must print both the position and the item in the collection

for idx, item in enumerate(instructor_set):
    print(f"{idx}: {item}")

for idx, item in enumerate(pm_tuple):
    print(f"{idx}: {item}")

for idx, item in enumerate(harry_list):
    print(f"{idx}: {item}")

for idx, key in enumerate(d):
    print(f"{idx}: {key}")


# + id="FjcZLRgMOQDL"
# - 4 mark
# Use the items() method of the dict class to enumerate a dictionary
# You must print the position, the key and the value

for idx, (key, value) in enumerate(d.items()):
    print(f"{idx}: {key} - {value}")

