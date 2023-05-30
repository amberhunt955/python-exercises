
def hello(age, name="my friend"):
    print('Hello ' + name + ", you are " + str(age) + " years old.")

hello(2)

# parameters vs arguments
# parameters are the values accepted by the function inside the function definition
# arguments are the values we pass to the argument when we call it

#* what we change inside the function doesn't affect outside the function (unless it is mutable, like a dictionary)
def change(value, dictionary):
    value = 2
    dictionary["name"] = "Anne"

val = 1
person = {"name": "Beau"}
change(val, person)
print(val) # returns 1
print(person)

#* a function can also return a value using the return statement

def getNum():
    num = 3
    return num

print(getNum())

def hi(name):
    if not name:
        return
    print("Hello " + name)

hi(False)
hi("anne")

#* Variable scope

# if you declare a variable outside a function - the variable is visible to any code running after the declaration, including functions (global variable)

# if you declare a variable inside a function - it's a local variable

#* Nested functions

# a function defined inside a function is visible only inside that function 

def talk(phrase):
    def say(word):
        print(word)
    
    words = phrase.split(' ')
    for word in words:
        say(word)
    
talk('I am going to buy the milk')

# using nonlocal to access a variable defined in the outer function from the inner function
def count():
    count = 0

    def increment():
        nonlocal count
        count = count + 1
        print(count)
    
    increment()

count()

#* Closures
# closure is a special way of doing a function in python

# if you return a nested function from a function, that nested function has access to the variables defined in that function, even if that function is not active anymore

def counter():
    count = 0

    def increment():
        nonlocal count
        count = count + 1
        return count

    return increment
    


increment = counter()

print(increment())
print(increment())
print(increment())
print(increment())
print(increment())