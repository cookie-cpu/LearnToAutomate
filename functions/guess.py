#Guess the number game program
import random
print('Hello! Enter your name:')
name = input()
print(name + ', I\'m thinking of a number between 1 and 10')
num = random.randint(1, 10)

for guessesTaken in range(1, 7):
  print('Take a guess')
  guess = int(input())

  if guess < num:
    print('Your guess is too low!')
  elif guess > num:
    print('Your guess is too low!')
  else:
    break #guess is correct, breaks from statement

if guess == num:
  print('good job! ' + name + ' you guessed the number in ' + str(guessesTaken) + ' guesses')
else:
  print('nope! the number i was thinking of was ' + str(num))

print('You took ' + str(guessesTaken) + ' guesses')