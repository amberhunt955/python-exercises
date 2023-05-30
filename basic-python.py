
#* Variables
  # - can't start with a number
  # - CAN have characters (letters), numbers, underscore
  # - can't have python keywords

#* Expressions -> code that returns a value
1+1
"Amber"

#* Statements -> An operation on a value
# Can have multiple statements on one line with a semicolon
# A program is formed by a series of statements
name = "Amber"; print(name)

#* In python, indentation matters
# Everything indented belongs to a block

#* Data types
print(type(name))
print(isinstance(name, str))

age = 2 # 2 is an int
print(isinstance(age, float)) # returns false

floatAge = float(2)
print(isinstance(floatAge, float)) # returns true

# str
# int
# float
# complex
# bool (for boolean)
# tuple (for tuples)
# range 
# dict (for dictionaries)
# set 

#* Operators 

# ======= Arithmetic operators =======

# -> + plus
# -> - minus
# -> * multiplication
# -> / division
# -> % remainder
# -> ** exponents
# -> // floor division (division then rounds down to nearest whole number)

age = 8
age *= 8 # age = age * 8

# ======= Comparison Operators =======

a = 1
b = 2

a == b #false
a != b #true
a > b #false
a <= b #true

# ======= Boolean Operators =======

# -> not
# -> and (only evaluates the second argument if the first one is true) (if x is false, then x, else, y)
# -> or (returns the value of the first operand that is not falsy, otherwise it returns the last operand) (if else is false, then y, else, x)

condition1 = True
condition2 = False

not condition1 #false
condition1 and condition2 #false
condition1 or condition2 #true

# ======= Bitwise Operators =======
# These are very rarely used

# -> & performs binary AND
# -> | performs binary OR
# -> ^ performs a binary XOR operation
# -> ~ performs a binary NOT operation
# -> << shift left operation
# -> >> shift right operation

# ======= is, in Operators =======

# -> "is" is the identity operator (used to compare two objects, returns true if both are the same object)
# -> "in"3 is the membership operator (used to tell if a value is contained in a list)

# ======= Ternary Operators =======
# Allows you to quickly define a conditional

def is_adult2(age):
  return True if age > 18 else False

#* Strings

# Multiline strings
print("""Beau is

39

years old.
""")

# Convert to upper/lower case
print("beau".upper())
print("bEAu".lower())

# Make first letter of each word capital
print("string title".title())

# Escape characters
name = "Be\"au" # include quotes
name = "Be\au" # new line
name = "Be\\au" # include backslash

#* Booleans (bool)
# Booleans have the first letter capitalized in python

# Numbers are always True, except 0

# Strings are false only when empty

# Lists. tuples, sets, dictionaries are false only when empty

#* Complex numbers

num1 = 2 + 3j
print(num1.real, num1.imag)
num2 = complex(2, 3)
print(num2.real, num2.imag)

#* Built in Functions

# absolute value
print(abs(-5.5))

# round
print(round(5.5))
print(round(5.49, 1)) 

# user input
# age = input("What is your age? ")
# print("Your age is " + age)

#* Control Statements

condition = True

if condition == True:
  print("The condition was true.")
else:
  print("The condition was false.")

# also elif (see rock paper scissors)

#* Lists
# Lists are an essential python data structure

dogs = ["Roger", 1, True, "Syd", 4]

print("Roger" in dogs)
print("Beau" in dogs)
print(dogs[0]) 
print(dogs[2:4]) # prints index 2-4
print(dogs[:3]) # prints up to 3
dogs.append("Judah")
print(len(dogs))
print(dogs)
dogs.extend(["Ashley", 2]) # add another list to existing list (can also do +=)
print(dogs)
dogs.remove(1)
print(dogs)
print(dogs.pop()) # removes last item from the list and returns it
dogs.insert(2, "Test") # add at a specific index
print(dogs)
dogs[1:1] = ["Test1", "Test2"] # add multiple at a specific index
print(dogs)

names = ["anne", "joe", "Elle", "bob"]
names.sort()
print(names)
# note that the sort method sorts uppercase letters first, then lowercase
# to get around this ->
names.sort(key=str.lower)
print(names) 

# you can copy a list
names_copy = names[:]
print(names_copy)

# the global sorted function returns a new list without modifying the original list
sorted(names, key=str.lower)

#* Tuples
# immutable groups of objects (can't add, remove, or alter items or their order)
# use parenthesis

people = ("Roger", "Syd", "Anne")
print(len(people))
print(sorted(people)) # prints modified but does not change original tuple

#* Dictionaries
# allow you to create key value pairs

dog = {"name": "Roger", "age": 8, "toy": "mouse", "birthday": "june 8"}

dog['name'] = "Syd"
print(dog.get("name"))
print(dog.get("color", "brown")) # return brown if no color
print(dog.pop("name")) # get and return popped item
print(dog)
print(dog.popitem()) # pop last item and return it
print(dog)
print("color" in dog) # in this case returns false
print(dog.keys()) # returns keys
print(list(dog.keys())) # returns keys in a list
print(dog.values()) # returns values
print(dog.items()) # returns all items in dictionary and convert it to a list
print(len(dog))
dog["favorite food"] = "meat" # add item to dictionary
print(dog)
del dog['age'] # delete item from dictionary
print(dog)
dogCopy = dog.copy()

#* Sets
# sets kind of work like tuples, but they're not ordered and they're mutable
# they are also kind of like dictionaries, but they don't have keys
# sets work well when you think of them as mathematical sets

set1 = {"Roger", "Syd"}
set2 = {"Roger"}
set3 = {"Luna"}

intersect = set1 & set2
print(intersect)

mod1 = set1 | set2 # this is called a union
mod2 = set1 | set3
print(mod1) # returns {"Syd", "Roger"}
print(mod2) # returns {"Luna", "Syd", "Roger"}

mod3 = set1 - set2 # find what is different between two sets
print(mod3)

# find if a set is a superset of another, and if a set is a subset of another
mod4 = set1 > set2
mod5 = set1 < set2
print(mod4)
print(mod5)

# make a set a list
print(list(set1))

# can use in operator to check if something is in set
print("Roger" in set1)

# IMPORTANT! a set cannot have two of the same item