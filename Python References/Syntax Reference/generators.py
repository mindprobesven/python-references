# ----------------------------------------------------------------------------------------------------------------
# Generator function
# ----------------------------------------------------------------------------------------------------------------

def countdown(n):
    print("Counting down from ", n)
    while n > 0:
        yield n
        n -= 1

x = countdown(10)
print(x.__next__()) # The generator funcion only execute on __next__()
print(x.__next__())
print(x.__next__())

x = countdown(10) # the generator is a one-time operation. It can only be iterated once.
print(x.__next__())
print(x.__next__())

# ----------------------------------------------------------------------------------------------------------------
# Generator expression
# ----------------------------------------------------------------------------------------------------------------

a = [1, 2, 3, 4]
b = (2*x for x in a)
print(b) # <generator object <genexpr> at 0x1067fdc50>

for i in b:
    print(str(i), end=" ")

print("\n")

# ----------------------------------------------------------------------------------------------------------------

log_file_data = [
    '81.107.39.38 - ... "GET /ply/ HTTP/1.1" 200 7587',
    '81.107.39.38 - ... "GET /favicon.ico HTTP/1.1" 404 133',
    '81.107.39.38 - ... "GET /ply/bookplug.gif HTTP/1.1" 200 -'
]

# creating a process pipeline
byte_column = (line.rsplit(None, 1)[1] for line in log_file_data) # byte_column is a generator
bytes_send = (int(x) for x in byte_column if x != '-')  # bytes-send is also a generator and iterates over the byte_column generator
print("Total: ", sum(bytes_send)) # the calculation is done in the last step
