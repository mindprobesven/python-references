# ----------------------------------------------------------------------------------------------------------------
# Returns a list of the results after applying the given function to each item of a given iterable (list, tuple etc.) 
# ----------------------------------------------------------------------------------------------------------------

def addition(n): 
    return n + n 

numbers = (1, 2, 3, 4)
result = map(addition, numbers)
print(list(result))

# With lambda
numbers = (1, 2, 3, 4)
result = map(lambda x: x + x, numbers)
print(list(result))

# Adding two lists with lambda
numbers1 = [1, 2, 3]
numbers2 = [4, 5, 6]

result = map(lambda x, y: x + y, numbers1, numbers2)
print(list(result))

# Listify with map
l = ['sat', 'bat', 'cat', 'mat']
# map() can listify the list of strings individually
test = list(map(list, l))
print(test)
