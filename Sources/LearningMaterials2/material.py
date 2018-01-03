# covered in this file

# functions
# user input
# more on strings
# file input/output

# ----------------------------------------------------------------


# functions
# ----------------------------------------------------------------

# functions allow you to reuse code you have written
# written as def, then the function name, then when it uses(parameters)
# return is used to yield a value to the caller of the function
def sum_two_values(a, b):
    total = a + b
    return total

print(sum_two_values(2, 2))

# can;t directly get value of a or b because they're in the function
# they're said to be out of scope
# print(total)

# defining variables outside of function works too!
sub = 0


def sub_two_values(b):
    sub = a - b
    return sub
print(sub_two_values(5, 2))

# functions are really good for helping to write more readable code
# ----------------------------------------------------------------


# user input
# ----------------------------------------------------------------

print('What is your age?')

# the following line stores everything typed up until ENTER
age = sys.stdin.readline()

# prints using user entered value
print('You are ', name, ' years old!')
# ----------------------------------------------------------------


# more on strings
# ----------------------------------------------------------------

my_string = 'hello world'

# returns the string length
print(len(long_string))

# strings can be indexed just like lists can
# this gets the first 4 characters of a string

print(my_string[0:4])

# you can index string using negative numbers too
# it can also be done with lists
# last index, [len(my_string) -1], is the same as saying [-1]

# get last 5 characters
print(my_string[-5:])

# Everything up to the last 5 characters
print(my_string[:-5])

# capitalize the first character in a string
print(my_string.capitalize())

# return the index of the start of the string
# case sensitive
print(my_string.find("hello"))

# returns true value if all characters are letters
print(my_string.isalpha())

# return true if all characters are alphanumeric
print(my_string.isalnum())

# returns the string length
print(len(my_string))

# replce a word in a string with another string
print(my_string.replace("hello", "goodbye"))

# remove white space from front and end
print(my_string.strip())

# split up a string into a list based on the delimiter
split_up = "john' number:01234567"
my_list = my_.split(":")
print(my_list)
# ----------------------------------------------------------------


# file input/output
# ----------------------------------------------------------------

# overwite or create a file for writing in
my_file = open("test.txt", "wb")

# get the file mode used
print(my_file.mode)

# get the name of the file
print(my_file.name)

# write text to a file with a newline at end
my_file.write(bytes("Write me to the file\n", 'UTF-8'))

# closing a file
my_file.close()

# open a file for reading and writing
my_file = open("other_file.txt", "r+")

# to just read the text from the file
read_text = other_file.read()

print(read_text)

# to delete the file
# to do this type 'import os' at the top of your file
os.remove("other_file.txt")
# ----------------------------------------------------------------

