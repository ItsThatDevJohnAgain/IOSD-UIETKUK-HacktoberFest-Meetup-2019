#python 3 

userEntry = input()
userAge = int(userEntry)

if userAge > 18:
  print("Adult. Congrats.")
elif (userAge > 10 and userAge <= 18):
  print("Teen. Rad, yo.")
elif (userAge < 10):
  print("Child. Cool.")
