print('How many cats do you have?')
numCats = input()
try:
  if int(numCats) >= 4:
    print('Thats a lot of cats')
  else:
    print('that is not many cats')
except ValueError:
  print('You did not enter a number')