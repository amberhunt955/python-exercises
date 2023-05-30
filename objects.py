
# Everything in python is an object, even values of basic primitive types, like integers, strings, floats

# Objects have attributes and methods that can be accessed using the dot syntax

age = 8 # age now has access to the properties and methods defined for all int objects

print(age.real)
print(age.imag)
print(age.bit_length()) # returns the num of bits necessary to represent this number in binary notation

items = [1, 2] # items has access to properties and methods defined for all list objects
items.append(3)
print(items)
items.pop()
print(items)

# the id global function in python lets you inspect the location in memory for a particular object
print(id(items))

# some objects are mutable while others are immutable, and that depends on the object itself
# if the object provides methods to change its content then its mutable - otherwise its not
# most types defined by python are immutable
  # int is immutable