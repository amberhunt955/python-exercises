
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
a <=b #true

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