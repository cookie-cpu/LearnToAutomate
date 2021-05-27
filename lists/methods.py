numbers = [1,2,3,4,5,6,7,8,9,10]
print(numbers.index(5))
numbers.append('definitely a number not a string')
print(numbers)
numbers.insert(5, 'spaghetti')
print(numbers)
numbers.remove(2)
print(numbers)


letters = ['a', 'b', 'c', 'd', 'e', 'f']
letters.sort(reverse=True)
print(letters)

spam = ['A','Z','a','z']
spam.sort(key=str.lower)
print(spam)