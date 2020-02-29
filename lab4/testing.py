from lab4 import findInnermost, reverseTuple, check, countwords

print('Question 1:\n')

one = [5]
two = [[55]]
three = [[[123]]]
four = [[[[[[[[18]]]]]]]]

print(findInnermost(one))
print(findInnermost(two))
print(findInnermost(three))
print(findInnermost(four))

print("\n\nQuestion 4 \n")

a = (1,2,3,4,5)
b = ('red', 'green','blue', 'yellow')

print(reverseTuple(a))
print(reverseTuple(b))


print("\nQuestion 3\n")

sub = 'a'
bigstring = 'hello all'

sub2 = 'b'
bigstring2 = "123534klkjdsakfje"

print(check(sub, bigstring))
print(check(sub2, bigstring2))

print('\nQuestion 4\n')

phrase = "Hello my name is"
phrase2 = 'A white cat and a black cow'
phrase3 = 'a b c de f g h'
phrase4 = "Orange you glad I didn't say banana"

print(countwords(phrase))
print(countwords(phrase2))
print(countwords(phrase3))
print(countwords(phrase4))

print("\nQuestion 5\n")

