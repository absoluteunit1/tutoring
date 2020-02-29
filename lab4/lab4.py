# Question 1

# Assume that L is a list with one element. The element might be a number or it might be a list
# of one element, where that element might be a number or a list of one element, and so on.
# Return the innermost number. You must use recursion. Your solution cannot use a loop.
# Hint: type(52) == int is True.
# Test your program with the following:
# [5]
# [[55]]
# [[[123]]]
# [[[[[[[[[[[[18]]]]]]]]]]]]

def findInnermost(l):
    if type(l) == int:
        return l
    return findInnermost(l[0])

# Question 2

# Assume that T is a tuple. Return a tuple which is the reverse of T. You must use recursion.
# Your solution cannot use a loop or a list or a built-in reverse function. Hint: Reverse the tuple
# starting at the second element, and concatenate to the end of that reversed tuple the first
# element.

def reverseTuple(t):
    if len(t) == 1:
        return (t[0],)
    return reverseTuple(t[1:],) + (t[0],)

# Question 3

# Assume that sub and bigstring are strings. Return True if sub is part of bigstring, False
# otherwise. You must use recursion. Your solution cannot use a string funtion or the 'in
# operation'. Your solution cannot use a loop. Hint: check if sub is the beginning of bigstring,
# and if not, consider the string obtained by removing the first letter from bigstring.

def check(a, b):
    pass