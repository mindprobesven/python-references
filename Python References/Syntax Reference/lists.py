thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist)

print(thislist[1])

# will start at index 2 (included) and end at index 5 (not included)
print(thislist[2:5])

# returns items from beginning to "orange"
print(thislist[:4])

# returns items from "cherry" to the end of list
print(thislist[2:])

# check if item is present in a list
if "apple" in thislist:
    print("Yes, apple is in the list")

# add item to the end of the list
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)

# add item at the specific index
thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")
print(thislist)

# remove an item
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)

# remove the last item
thislist = ["apple", "banana", "cherry"]
thislist.pop()
print(thislist)

# remove item at specific index
thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)

thislist = ["apple", "banana", "cherry"]
del thislist[1]
print(thislist)

# clear a list
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)

# copy a list
thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)

thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
print(mylist)

# join two lists
list1 = ["apple", "banana", "cherry"]
list2 = ['Sven', 'Barbara', 'Valentina']
list3 = list1 + list2
# or
list3 = list1.append(list2)
print(list3)

list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]
list1.extend(list2)
print(list1)

# the list constructor
thislist = list(("apple", "banana", "cherry"))

# more list methods
# count()
# reverse()
# sort()
