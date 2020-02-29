
def readFile(fileName):
    key_list = list(open(fileName, 'rb').read()) # we convert the text elment into the list of bytes
    key = {} # create an empty dictinoary 
    for i in range(256): # iterate from 0 to 256
        key['i'] = key_list[i] # create key value pairs; each key is what the value encryption is.
    return key # returns the dictionary with the matching key value pairs

def writeFile(fileName, content):
    textFile = open(fileName, 'rb+') # Open the text file itself
    for byte in content: # writes each byte element in the content into textfile
        textFile.write(byte) # writes the binary to the file
    
def encrypt(plainText, key):
    content = list(open(plainText, 'rb').read()) # get the content of the plainText as a list of bytes
    encrypted_content = [] # create a new list of the list of bytes
    for i in range(len(content)): # create a for loop to iterate thtough each element in the content list 
        encrypted_content.append( key[content[i]] ) # change the plain text value to its byte equivalent and gets it ciphered byte
    return encrypted_content # return encrypted list in bytes

def decrypt(cipherText, key):
    content = list(open(cipherText, 'rb').read()) # turn the content of the text into a bytes format
    decrypted = [] # create a decryted list to store the decrypted bytes into
    for i in range(len(content)): # for every encrypted element in the cipherText (by the index)...we iterate through each element using a for loop
        decrypted.append(key.index(content[i])) # We take the encrypted value and make it equal to the index of that element in the key (decrypting it)
    return decrypted # returns the decrypted cipher


