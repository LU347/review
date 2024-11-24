#Data Types
# text: str
# numeric: int, float, complex
# sequence: list, tuple, range
# mapping: dict
# set types: set, frozenset
# boolean: bool
# binary types: byte, bytearray, memoryview
# none: NoneType

#Getting the data type
x = 5
print(type(x))

#Setting the specific data type
x = complex(1j)

#Casting

#Strings
print("My name is 'Lucile'")
#or
print('My name is "Lucile"')

# slicing strings
b = "Hello World"
print(b[2:5]) #5 not included
print(b[:5])
print(b[2:])

#Negative indexes start from the end of the string
print(b[-5:-2])

#String Methods
# .lower() .upper() .strip() .replace(needle, newStr)
# .split(delimiter)

#Concatenate str  with +
newStr = "helo" + " " + "world"
print(newStr)

#F-Strings
# latest way of formatting strings
age = 99
s = f"My name is lucile and I am {age} years old"
# shortening decimals .. f"{float.2f}"

#Lists
# indexed, allows duplicates, changeable
thislist = ["apple", "bottom", "jeans"]
print(len(thislist))

#Tuples
# ordered, unchangeable, allows duplicates
mytuple = ("apple", "bottom", "jeans")
print(len(mytuple))
#if you need to update an element in the tuple you have to convert it to a list
#update it, then convert it back into a tuple

#Set
# unordered, items are unchangeable, unindexed, no duplicates
thisset = {"apple", "banana", "cherry"}
print(thisset)

#Dictionary
# ordered (3.7+), changeable, no duplicates

