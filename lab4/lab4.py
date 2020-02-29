# Question 1

# Assume that L is a list with one element. The element might be a number or it might be a list
# of one element, where that element might be a number or a list of one element, and so on.
# Return the innermost number. You must use recursion. Your solution cannot use a loop.
# Hint: type(52) == int is True.
# Test your program with the following:


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
    if a == b[0:len(a)]:
        return True
    elif len(a) == len(b) and a != b:
        return False
    return check(a, b[1:])

# Question 4

# Assume that a phrase is a string. Return the number of words in phrase. Assume that words are
# separated by one or more blanks. You are not allowed to use the built-in function split() For
# example, countwords('The cat is black') would return 4. countwords('The cat is black') would
# also return 4. countwords('A whitecat and a black cow.') would also return 7.
# Test your program with the following:

def countwords(phrase):
    pass
    # still working on it

# Question 5

# Return the first value of n such that the sum
# Sum = 4/1 - 4/3 + 4/5 - 4/7 + ... + 4 * (-1)**(n+1)/(2n - 1)
# is within epsilon of math.pi = 3.141592653589793 For example, if epsilon is 1, then return 1,
# since 4 is within 1 of pi. If epsilon is 0.5 then return 2, since 4 is not within 0.5 of pi but 4 - 4/3
# = 2.67, and that is within 0.5 of pi

def notSure(huh):
    pass



