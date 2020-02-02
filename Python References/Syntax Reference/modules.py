from functions import buildUserProfile as userInfo

user = userInfo('Sven', 'Kohn', occupation='Engineer', age=39)

for key, value in user.items():
  print(f"{key}: {value}")