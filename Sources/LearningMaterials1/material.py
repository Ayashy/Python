# covered in this file

# printing and variables
# arithmetic
# lists
# tuples
# dictionaries
# if/else statements
# loops
# ----------------------------------------------------------------


# printing and variables
# ----------------------------------------------------------------

# print() is a statement that outputs data to the screen
# something inside quotation marks is called a String
print("Hello World")

'''
This is a multi-line comment
'''

# A variable is a place to store a value
# Its name is like a label for that value

name = "So You Want To Code"

print(name)

# A variable name can hold letters, numbers, or special characters
# variable names cannot start with a number

# There are five built in data types: Numbers, Strings, List, Tuple, Dictionary
# You can store any data type in any variable

name = 15
print(name)
# ----------------------------------------------------------------


# arithmetic
# ----------------------------------------------------------------

# There are a few arithmetic operators
# they are:   +, -, *, /, %, **, //
# ** is Exponential
# // is Floor Division

print("2 + 2 =", 2+2)
print("4 - 2 =", 4-2)
print("5 * 2 =", 5*2)
print("6 / 2 =", 6/2)
print("7 % 2 =", 7 % 2)
print("2 ** 2 =", 2**2)
print("9 // 2 =", 9//2)
print("5 / 2.0 =", 5/2.0)
print("5 + 3 * 2 / 6 - 4 =", 5+3*2/6-4)

#  * and / are always performed before + and -

# A string is a sequence of characters surrounded by " or '
# To keep from printing newlines use end=""
print("I don't like ", end="")

# printing a string multiple times with *
print('\n' * 5)
# ----------------------------------------------------------------


# lists
# ----------------------------------------------------------------

# sometimes called arrays
# a list is a collection of values you can maniplulate
# you can put any data type in a list
# Each value has an index in the list
# the first index is 0, then 1 etc.

shopping_list = ['Apples', 'Oranges', 'Bananas', 'Pears', 'Blueberries']

print('The first item is', shopping_list[0])

# You can change the value stored at any index of a list
shopping_list[0] = "Apple Juice"

# You can get a subset of the list
# this works by giving two indexes
# [min:up to but not including the max]
print(shopping_list[1:4])

# You add values to a list using append
shopping_list.append('Cherries')

# Insert item at  any given index
shopping_list.insert(3, "Strawberries")

# Remove any item from list
shopping_list.remove("Oranges")

# sort.() sorts items in list
# if strings, sorts alphabetically
# if integers, sorts from lowest to highest
shopping_list.sort()

# Reverse sort items in list
# the reverse of above for strings and integers
shopping_list.reverse()

# del deletes an item at a given index
del shopping_list[2]

#  to Get length of list wrap the list as follows
print(len(shopping_list))
# ----------------------------------------------------------------


# tuples
# ----------------------------------------------------------------

# Values in tuples can't change like lists can
# lists are mutable
# tuples are immutable

a_tuple = (3, 1, 9, 10, 3)

# make a tuple into a list
my_tuple = list(a__tuple)

# Convert a list into a tuple
my_list = tuple(shopping_list)

# tuples have len(tuple), min(tuple) and max(tuple)
# ----------------------------------------------------------------


# dictionaries or maps
# ----------------------------------------------------------------

# each value has unique key
# like a list but cannot be joined with +

words = {"hello": "bonjour", "goodbye": "au revoir",
         "that's life": "c'est la vie"}

print(words['hello'])

# Delete an entry in the data structure
del words["that's life"]
print(words)

# Replace a value
super_villains['hello'] = 'salut'

# Print the number of items in the dictionary
print(len(words))

# Get the value for a key
print(wordss.get("goodbye"))

# Get a list of  all dictionary keys
print(words.keys())

# Get a list of all dictionary values
print(words.values())
# ----------------------------------------------------------------


# if/else statements
# ----------------------------------------------------------------

# three statements - if, else and elif
# they help perform actions based off of conditions
# the comparisonpOperators : ==, !=, >, <, >=, <=

# an statement will execute code if it's condition is met
# White space is used to group blocks of code in Python
# Use the same indentation for blocks of code
# python is a stickler for indentation

age = 69
if age > 50:
    print('You are over half a century old')

# if a condition is not met, use else
# else comes after and if statement
if age > 50:
    print('You are over half a century old')
else:
    print('You are not over half a century old')

# If you want to check for more conditions, use elif
# If the first condition matches it won't check conditions that follow

if age > 50:
    print('You are over half a century old')
elif age == 50:
    print('You are exactly half a century old')
else:
    print('You are not over half a century old')

# You can combine conditions with logical operators
# Logical Operators : and, or, not

year_born = 1996
if ((year_born >= 1990) and (year_born <= 1999)):
    print("You were born in the 90's")
else:
    print("You weren't vorn in the 90's")
# ----------------------------------------------------------------


# loops
# ----------------------------------------------------------------
# two types - for loops and while loops
# loops let you to perform an action a set number of times

# for loops
# range performs the action 10 times if set between 0 - 9
for number in range(0, 10):
    print(number, ' ', end="")

# You can use for loops to run through a list
shopping_list = ['Apples', 'Oranges', 'Bananas', 'Pears', 'Blueberries']

for item in grocery_list:
    print(item)

# You can also define a list to run through like this
for number in [2, 4, 6, 8, 10]:
    print(number)

# you can nest one loop within another like this
for x in range(0, 3):
    for y in range(0, 3):
        print(x * y)

# while loops
# while loops used when you don't know amount of times you have to loop

# get a random number using random.randrange()
# here we generate a random number between 0 and 100
random_num = random.randrange(0, 100)

# for this while loop if random number is 50, it will stop
while (random_num != 50):
    print(random_num)
    random_num = random.randrange(0, 100)

# an iterator for a while loop, i, is defined beforehand
i = 0
while (i <= 11):
    if(i % 2 == 0):
        print(i)
    elif(i == 11):
        # break forces a loop to stop
        break
    else:
        # pass does nothing
        pass
    i = i + 1
