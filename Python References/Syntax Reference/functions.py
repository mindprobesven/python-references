# default parameter
def my_function(country="Norway"):
    print(country)

# keyword arguments (kwargs)
def x(a, b, c):
    print(a, b, c)

x(a="a", b="b", c="c")

# arbitrary arguments
def y(*kids):
    print(kids[2])

y("a", "b", "c", "d", "e")

# Creates a dictionary for userInfo
def buildUserProfile(first, last, **userInfo):
    userInfo['first'] = first
    userInfo['last'] = last
    return userInfo

user = buildUserProfile('Sven', 'Kohn', occupation='Engineer', age=39)

for key, value in user.items():
    print(f"{key}: {value}")
