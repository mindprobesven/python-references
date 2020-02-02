try:
    print(x)
except:
    print("An exception has occured")

# many exceptions
try:
    print(x)
except NameError:
    print("Variable x is not defined")
except:
    print("Something else went wrong")

# else
try:
    answer = 5 / 0
except ZeroDivisionError:
    print("You can't devide by zero!")
else:
    print(answer)

# pass
try:
    answer = 5 / 0
except ZeroDivisionError:
    # This will fail silently and continue with the code
    pass
else:
    print(answer)

print("---------")

# finally
try:
    f = open("demofile.txt")
    f.write("Lorum Ipsum")
except FileNotFoundError:
    print("Something went wrong when writing to the file")

finally:
    try:
        f.close()
    except NameError:
        print("Something went wrong when writing to the file")

# raise an exception
x = "hello"

if type(x) is not int:
    raise TypeError("Only integers are allowed")
