# def eggs(cheese):
#   cheese.append('Hello, world')

# spam = [1,2,3]
# eggs(spam)
# print(spam)

import copy
spam = ['A','B','C','D','E']
cheese = copy.deepcopy(spam)
cheese[1] = 42
print(cheese)
print(spam)