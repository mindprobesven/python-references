import time

def pretty_sumab(func):
    def inner(a, b):
        print(f"{str(a)} + {str(b)} is ", end="")
        return func(a, b)
    return inner

@pretty_sumab
def sumab(a, b):
    summed = a + b
    print(summed)

# -------------------------------------------------

def measure_time(func):
    def wrapper(*arg):
        t = time.time()
        resp = func(*arg)
        print(f"Function took {str(time.time() - t)} seconds to run.")
        return resp
    return wrapper

@measure_time
def my_function(n):
    time.sleep(n)
    return "Done"

if __name__ == "__main__":
    sumab(5, 2)
    RESPONSE = my_function(1)
    print(RESPONSE)
