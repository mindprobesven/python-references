# Creating an immutable list

tubleList = (200, 50)

for tuble in tubleList:
  print(tuble)

# This will fail because tubles are immutable
# tubleList[0] = 100

tubleList = (100, 99)

# Iterrating over a tuble is possible
for tuble in tubleList:
  print(tuble)
  