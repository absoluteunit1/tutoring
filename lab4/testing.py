from lab4 import findInnermost, reverseTuple 

print('Question 1:\n')

one = [5]
two = [[55]]
three = [[[123]]]
four = [[[[[[[[18]]]]]]]]

print(findInnermost(one))
print(findInnermost(two))
print(findInnermost(three))
print(findInnermost(four))

print("\n\n")

print('Question 2\n')

a = (1,2,3,4,5)
b = ('red', 'green','blue', 'yellow')

print(reverseTuple(a))
print(reverseTuple(b))

print('\n')

print("Question 3\n")

sub = 'a'
bigstring = 'hello all'

print(check(sub, bigstring))

print('\n')
