# Lits and Tuples


    # 1. Lists are ordered.
    # 2 .Lists can contain any arbitrary objects.
    # 3. List elements can be accessed by index.
    # 4. Lists can be nested to arbitrary depth.
    # 6. Lists are dynamic.

# Tuples:

# Tuples are identical to lists in all respects, except for the following properties:

#     Tuples are defined by enclosing the elements in parentheses (()) instead of square brackets ([]).
#     Tuples are immutable.


# 3. Indexing Lists

a = [1,2,3]
a[0] # to get first element
a[2] # last element

# 5. Mutating Lists

a[1] = "hell0"

# Tuples vs Lists

tupleA = (1,2,3,4)
listA = [1,2,3,4]

listA[0] = 'hello'
# tupleA[0] = 'hello' gives an error because tuples are immutable. Cannot modify or change elements in a tuple

# 6. Lists and tuples dynamic

a = [1, ["hi", "hello"], "cheese", (5,6,7)]

tupleb = (1, "hello", [1,2,3])
