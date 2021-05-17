spam = 0
while spam < 5:
  spam = spam+1
  if spam == 3:
    continue #breaks loop and starts at beginning, 'spam is 3' is never printed
  print('spam is ' + str(spam))