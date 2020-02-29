def reverse(str1):
    return str1[::-1]

def palindrome(str1):
    str2=reverse(str1)
    if str2==str1:
        print ('palindrome')
    else:
        print('incorrect')

def palindrome2(str1):
    return reverse(str1) == str1

palindrome('dad')
palindrome('hejllo')