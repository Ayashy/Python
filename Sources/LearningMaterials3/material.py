# covered in this file

# classes and objects
# inheritence
# polymorphism

# ----------------------------------------------------------------

# classes and objects
# ----------------------------------------------------------------

# time for object orientated programming (OOP)
# OOP allows us to write real world things, or objects, with code!
# an object has attributes (color, height, weight) which are object variables
# an object has abilities (walk, talk, eat) which are functions or methods


class Person:
    # None signifies the lack of a value
    # make a variable private by starting it with __
    # otherwise it's public
    __name = None
    __student_number = None
    __height = None
    __weight = None
    __sound = None

    # a constructor is called to set up or initialize an object
    # self allows an object to refer to itself inside of the class
    def __init__(self, name, student_number, height, weight):
        self.__name = name
        self.__s_number = student_number
        self.__height = height
        self.__weight = weight

    def set_name(self, name):
        self.__name = name

    def set_student_number(self, student_number):
        self.__s_number = student_number

    def set_height(self, height):
        self.__height = height

    def set_weight(self, weight):
        self.__height = height

    def get_type(self):
        print("Person")

    def get_name(self):
        return self.__name

    def get_student_number(self):
        return self.__s_number

    def get_height(self):
        return str(self.__height)

    def get_weight(self):
        return str(self.__weight)

    # this to_string method only uses name and student number
    # you could use other attributes I have set if you wanted
    # you can use as many as you want
    def to_string(self):
        return "{} has student number {}".format(self.__name, self.__st_number)

# create a Person object
person1 = Person('John', 1399878, 170, 80)

print(person1.to_string())

# can't access this value directly because it is private not public
# print(person1.__name)
# ----------------------------------------------------------------


# inheritence
# ----------------------------------------------------------------
# you can inherit all of the variables and methods from another class

class Male(Person):
    __age = None

    def __init__(self, name, student_number, height, weight, age):
        self.__age = age

        # call the super class, in this case Male, constructor
        super(Male, self).__init__(name, student_number, height, weight, age)

    def set_age(self, age):
        self.__age = age

    def get_age(self):
        return self.__age

    def get_type(self):
        print ("Male")

    # we can overwrite functions in the super class
    def to_string(self):
        return "{} is {} years old".format(self.get_name(), self.get_age())

person1 = Male('John', 1399878, 170, 80, 27)

print(person1.toString())
# ----------------------------------------------------------------


# polymorphism
# ----------------------------------------------------------------

# polymorphism allows use to refer to objects as their super class
# this lets you get correct functions are called automatically

# imagine we have an animal object with attributes, name, age, owner
# imagine this object has super classes like Dog, Cat and Pig
class AnimalTesting:
    def get_type(self, animal):
        animal.get_type()

test_animals = AnimalTesting()
bruno = Dog('bruno', '4', 'John')
test_animals.get_type(spot)
spot.get_owner()

# try writing your own object for animal following the person object
# then try writing your own super Dog following the Male object
