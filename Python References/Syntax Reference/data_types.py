# ----------------------------------------------------------------------------------------------------------------
# complex number
# ----------------------------------------------------------------------------------------------------------------
x = 1j
# Returns data type
print(1 + x, "is of type", type(x))
# Checks for data type
print(x, "is a complex number?", isinstance(x, complex))

# ----------------------------------------------------------------------------------------------------------------
# tuple
# ----------------------------------------------------------------------------------------------------------------
# an ordered sequence of items same as list that is immutable
x = (1, 2, 3)

# ----------------------------------------------------------------------------------------------------------------
# set
# ----------------------------------------------------------------------------------------------------------------
# an unordered collection of unique items.
x = {"apple", "banana", "cherry"}
print("a = ", x)

# set eliminates duplicates
x = {1, 1, 2, 2, 3, 3, 3, 4, 5, 5, 5, 5, 6}
print(x)

# sets have operations such as union and intersection.
set1 = {1, 2, 3, 4, 5}
set2 = {1, 3, 3, 5, 6}
set1 |= set2
print(set1)

# union() returns a new set with all items from both sets
set1 = {1, 2, 3, 4, 5}
set2 = {1, 3, 3, 5, 6}
set3 = set1.union(set2)

# loop through set
for x in set1:
    print(x)

# check if banana is present in the set
x = {"apple", "banana", "cherry"}
print("banana" in x)

# add one item
x = {"apple", "banana", "cherry"}
x.add("orange")
print(x)

# add multiple items
x = {"apple", "banana", "cherry"}
x.update(["orange", "mango", "grapes"])
print(x)

# remove item
x = {"apple", "banana", "cherry"}
x.remove("banana")
print(x)

# remove the last item in the set. Sets are unordered so it is unknow what item gets removed.
x = {"apple", "banana", "cherry"}
x.pop()
print(x)

# empty a set
x = {"apple", "banana", "cherry"}
x.clear()
print(x)

# delete set completely
x = {"apple", "banana", "cherry"}
del x
# print(x) = error: x is not defined

# the set() constructor
x = set(("apple", "banana", "cherry"))
print(x)

# set has many methods, some are
# difference()
# intersection()
# issubset()
# symmetric_difference()
# etc.

# ----------------------------------------------------------------------------------------------------------------
# frozenset
# ----------------------------------------------------------------------------------------------------------------
# an unordered collection of unique items that is immutable
x = frozenset(("apple", "banana", "cherry"))
print(x)

# ----------------------------------------------------------------------------------------------------------------
# bytes - is immutable
# bytes objects are immutable sequences of integers, each value in the sequence
# ----------------------------------------------------------------------------------------------------------------

# create a byte of a given integer size
x = bytes(5)
print(x) # b'\x00\x00\x00\x00\x00'

# create a bytes object
x = b'Sven'
print(x) # b'Sven'

# triple singe quotes allow multiple lines
x = b'''Sven,
rocks,
at,
Python'''
print(x) # b'Sven,\nrocks,\nat,\nPython'

# convert iterable list to bytes
x = [1, 2, 3, 4, 5]
y = bytes(x)
print(y) # b'\x01\x02\x03\x04\x05'

# convert string to bytes
x = "El niño come camarón"
y = bytes(x, 'utf-8')
print(y) # b'El ni\xc3\xb1o come camar\xc3\xb3n'

# Create a string using the decode() method of bytes
x = b'El ni\xc3\xb1o come camar\xc3\xb3n'
y = x.decode('utf-8')
print(type(y))
print(y) # El niño come camarón

# convert hex string to bytes
x = '7376656e7376656e7376656e' # a string with hexadecimal data
# the string must contain two hexadecimal digits per byte e.g. "+" = 2b
y = bytes.fromhex(x)
print(y) # b'svensvensven'

# retrun an integer representing the Unicode code point of that character
x = ord(b'm')
print(x) # 109

# generate a list of Unicode codes from the characters of bytes
x = b'Sven'
y = list(x)
print(y) # [83, 118, 101, 110]

# define a mapping table fo characters for use with a bytes object
bytes_table = bytes.maketrans(b'abcdef', b'uvwxyz')
print(bytes_table) # prints out the mapping configuration
text = "Sven loves to program with Python"
b_new = text.translate(bytes_table)
print(b_new) # Svyn lovys to progrum with Python

#convert bytes to hex
import binascii
string_to_hex = binascii.hexlify("sven".encode('utf8'))
print(string_to_hex) # b'7376656e'
hex_to_string = binascii.unhexlify(b'7376656e')
print(hex_to_string) # b'sven'
print(hex_to_string.decode('utf-8')) # sven

# return a single character based on the integer value
x = chr(50)
print(x) # 2

# get the character from the Unicode numeric code in a bytes object
x = [83, 118, 101, 110]
y = bytes(x)
print(y) # b'Sven'

# ----------------------------------------------------------------------------------------------------------------
# bytesarray - is mutable
# ----------------------------------------------------------------------------------------------------------------

# create a bytes object with character Unicode codes
a = list(bytes("Sven loves to program with Python", 'utf-8'))
print(a) # [83, 118, 101, 110, 32, 108, 111, 118, 101, 115, 32, 116, 111, 32, 112, 114, 111, 103, 114, 97, 109, 32, 119, 105, 116, 104, 32, 80, 121, 116, 104, 111, 110]

# convert bytes to bytesarray
y = bytearray(a)
print(y) # bytearray(b'Sven loves to program with Python')

# remove items
del y[5:11]
print(y) # bytearray(b'Sven to program with Python')

# add items
y[5:15] = b"loves"
print(y) # bytearray(b'Sven loves with Python')

# use any methods of mutuable lists
y.append(45)
y.append(45)
y.append(45)
print(y) # bytearray(b'Sven loves with Python---')

# ----------------------------------------------------------------------------------------------------------------
# memoryview - works with bytes and bytearray. Modifications are only possible on bytearray.  
# ----------------------------------------------------------------------------------------------------------------

randomByteArray = bytearray('ABC', 'utf-8')
print(list(randomByteArray)) # This would create a copy of the byte object. Not good if we are dealing with large amounts of data e.g. binary data of an image.

# to avoid creating a copy, we use memoryview() to access the buffer of an object
# The memoryview() method returns a memory view object of the given object.
mv = memoryview(randomByteArray)
print(mv) # <memory at 0x10af85a10>

print(mv[0]) # 65
# create a byte from memory view
print(bytes(mv[0:2])) # b'AB'
# creat a list from memory view
print(list(mv[0:3])) # [65, 66, 67]

# modify internal data using memory view
print(randomByteArray) # bytearray(b'ABC')
mv[1] = 90 # this only works on a bytearray (mutable). A byte would give a TypeError: cannot modify read-only memory
print(randomByteArray) # bytearray(b'AZC')
