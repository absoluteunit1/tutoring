
# Question 1

def findInnermost(l):
    if type(l) == int:
        return l
    return findInnermost( l[0] )

# Question 2

def reverseTuple(t):
    if len(t) == 1:
        return (t[0],)
    return reverseTuple(t[1:],) + (t[0],)

    