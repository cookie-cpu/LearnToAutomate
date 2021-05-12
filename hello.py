#Program that says hello and asks for your name and age.

print('Hello world!')


print('What is your name?')
myName = input()
print('Good to meet you, ' + myName)
print('Your name length is: ')
print(len(myName))


print('What is your age?')
myAge = input()
print('You will be ' + str(int(myAge) + 1) + ' in a year')