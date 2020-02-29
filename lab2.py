# Number 1

def dec_to_bin(number):
    binary = ''
    while number != 0 :
        if number%2 == 1 :
            binary += '1'
        else:
            binary += '0'
        number = number//2
    return binary[::-1]
print(dec_to_bin(87324834345))
print(bin(87324834345))

# Number 2

def find_root(x):
    f = x**5 + 52*x**3 - 29
    epsilon = 0.01
    numOfGuesses = 0 
    low = 0.0
    high = max(1.0, x)
    ans = (high + low)/2

# Number 3

