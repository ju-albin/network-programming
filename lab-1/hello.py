# ============================================================
# 1.3.1 Numbers
# ============================================================

print(2 / 2)      # 1.0
print(2 / 3)      # 0.6666666666666666
print(2 // 3)     # 0
print(2 ** -1)    # 0.5


# ============================================================
# 1.3.2 Strings
# ============================================================

print(15 * "spam ")

# Multi-line string
str1 = """
This is a multi-line string.
It can span multiple lines.
"""

# Strings containing quotation marks
str2 = 'Han sa "Hej"'
str3 = "Han sa \"Hej\""

str4 = "Hello, world!"

# String slicing/indexing
print(str4[0:5])   # Hello
print(str4[:5])    # Hello
print(str4[-1])    # !
print(len(str4))   # 13

# Strings are immutable
# str4[0] = "J"


# ============================================================
# 1.3.3 Lists
# ============================================================

a = [100, 1, 2, 3, 4, 5, 6, 7]

r = a
s = a[0:3]
t = a[:]

a[0] = 99

print(a)  # [99, 1, 2, 3, 4, 5, 6, 7]
print(r)  # [99, 1, 2, 3, 4, 5, 6, 7]
print(s)  # [100, 1, 2]
print(t)  # [100, 1, 2, 3, 4, 5, 6, 7]

# Length of list
print(len(a))  # 8

# Nested lists
m = [[1, 2], [3, 4]]

print(m[1][0])  # 3


# ============================================================
# 1.3.4 First Steps
# ============================================================

# Swap two variables
a = 5
b = 10

print(a, b)  # 5 10

a, b = b, a

print(a, b)  # 10 5

# Print numbers 1-9 using a while loop
i = 1

while i <= 9:
    print(i)
    i += 1


# ============================================================
# 1.4.1 If Statements
# ============================================================

x = 2

if x == 1:
    print("one")
elif x == 2:
    print("two")
else:
    print("other")


# ============================================================
# 1.4.2 For Statements
# ============================================================

# Iterate through a list
animals = ["dog", "cat", "elephant"]

for animal in animals:
    print(animal)

# Create a copy of a list while iterating
words = ["cat", "dog", "fish"]

for word in words[:]:
    print(word)


# ============================================================
# 1.4.3 The range() Function
# ============================================================

# Print numbers 0-99
for i in range(100):
    print(i)

# Create a list containing 0-99
numbers = list(range(100))


# ============================================================
# 1.4.4 Break, Continue and Else Clauses on Loops
# ============================================================

for i in range(5):
    print(i)
else:
    print("Loop finished")


# ============================================================
# 1.4.5 Pass Statements
# ============================================================

pass # Just a placeholder, does nothing


# ============================================================
# 1.4.6 Defining Functions
# ============================================================

def hello(n):
    for i in range(n):
        print("parrot")

f = hello
f(3)  # prints "parrot" three times


## How are local variables stored? Explain the difference between stack and heap memory. How does this differ from languages like C/C++?
# Local cariables are stored as references to objects
# Objects are typically stored in the heap, and are garbage collected when no longer referenced
# Unlike C/C++ Python handles memory management for you so you dont have to worry about it.
# Unfortunately this leads to Python being slower than C/C++


## How do you access a global variable from inside a function, and how do you modify it?
x = 20
def my_function():
    global x
    # Read global variable
    print (x) # 20

    # Modify global variable
    x = 10
    print (x) # 10

## If a list named animal is passed to a function, how can the function add "flea" to the list?
def add_flea(animal):
    animal.append("flea")

# ============================================================
# 1.4.7 More on Defining Functions
# ============================================================

def print_all(*args):
    for arg in args:
        print(arg)

## Lambda functions are small functions that can be defined on one line
f = lambda a,b: a+b
print (f(2,3)) # 5

def hello():
    """Prints 'Hello, world!'"""
    print("Hello, world!")
print(hello.__doc__)  # Prints the docstring of the function

def greet():
    """Returns a greeting string"""
    return "Hello, world!"
print(greet.__doc__)  # Prints the docstring of the function
print(greet())  # Prints the return value of the function

# ============================================================
# 1.4.8 Intermezzo: Coding style
# ============================================================

# Python recommends using 4 spaces for indentation

# Visual studio code uses spaces by defauult.

