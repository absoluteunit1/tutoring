def findHighestOccur(n):
    zero = 0
    one = 0
    two = 0
    three = 0
    for i in str(n):
        if i == "0":
            zero += 1
        elif i == "1":
            one += 1
        elif i == "2":
            two += 1
        elif i == "3":
            three += 1
    countList = [zero, one, two, three]
    highest = max(countList)
    index = countList.index(highest)
    return index

print(findHighestOccur(3111122110))