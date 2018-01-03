
# This cheatsheet contains the folowing elements

# Lists : 
# Dictionaries : 
# Tuples :


# ---------------------------------------------------------------- #
#                        LISTS
# ---------------------------------------------------------------- #

# Lists or arrays are mutable ordered collection of items

a = ['red', 'blue', 'green']       # manually initialization
b = list(range(5))                 # initialize from iteratable
c = [nu**2 for nu in b]            # list comprehension (building a list)
d = [nu**2 for nu in b if nu < 3]  # conditioned list comprehension
e = c[0]                           # access element
f = c[1:2]                         # access a slice of the list
g = c[-1]                          # access last element
h = ['re', 'bl'] + ['gr']          # list concatenation
i = ['re'] * 5                     # repeat a list
['re', 'bl'].index('re')           # returns index of 're'
a.append('yellow')                 # add new element to end of list
a.extend(b)                        # add elements from list `b` to end of list `a`
a.insert(1, 'yellow')              # insert element in specified position
're' in ['re', 'bl']               # true if 're' in list
'fi' not in ['re', 'bl']           # true if 'fi' not in list
sorted([3, 2, 1])                  # returns sorted list
a.pop(2)                           # remove and return item at index (default last)
a.remove('item5')                  # remove a value from a list
del a[1]                           # delete an element from a list
a.reverse()                        # reverse a list


# ---------------------------------------------------------------- #
#                        Dictionaries
# ---------------------------------------------------------------- #

# Dictionary = Collection of key:value pairs + Mutable

a = {'red': 'rouge', 'blue': 'bleu'}         # create a new dictionatry
b = a['red']                                 # access value using key
'red' in a                                   # true if dictionary a contains key 'red'
c = [value for key, value in a.items()]      # loop through contents
d = a.get('yellow', 'no translation found')  # return default
a.update({'green': 'vert', 'brown': 'brun'}) # update dictionary by data from another one
a.keys()                                     # get list of keys
a.values()                                   # get list of values
a.items()                                    # get list of key-value pairs
del a['red']                                 # delete key and associated with it value
a.pop('blue')                                # remove specified key and return the corresponding value

# ---------------------------------------------------------------- #
#                        Tuples
# ---------------------------------------------------------------- #

# Tuples is same as a list but is immutable and ordered


tpl=(1,2,3,'a')                               # Create a tuple
new_list=list(tpl)                            # Converting tuple to list
new_tuple=tuple(new_list)                     # Converting list to tuple

# ---------------------------------------------------------------- #
#                        Sets
# ---------------------------------------------------------------- #

# A set is MUTABLE UNORDERED NO DUPLICATE
# Items must be hashable because hashlookup is used to get the items

a = {1, 2, 3}                                # initialize manually
b = set(range(5))                            # initialize from iteratable
a.add(13)                                    # add new element to set
a.discard(13)                                # discard element from set
a.update([21, 22, 23])                       # update set with elements from iterable
a.pop()                                      # remove and return an arbitrary set element
2 in {1, 2, 3}                               # true if 2 in set
5 not in {1, 2, 3}                           # true if 5 not in set
a.issubset(b)                                # test whether every element in a is in b
a <= b                                       # issubset in operator form
a.issuperset(b)                              # test whether every element in b is in a
a >= b                                       # issuperset in operator form
a.intersection(b)                            # return the intersection of two sets as a new set
a.difference(b)                              # return the difference of two or more sets as a new set
a - b                                        # difference in operator form
a.symmetric_difference(b)                    # return the symmetric difference of two sets as a new set
a.union(b)                                   # return the union of sets as a new set
c = frozenset()                              # the same as set but immutable



# ---------------------------------------------------------------- #
#                        Manipulating containers
# ---------------------------------------------------------------- #

#loop throught
for item in new_list:
    pass
#loop index+item
for index,item in enumerate(new_list):
    pass

