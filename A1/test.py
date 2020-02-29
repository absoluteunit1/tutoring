from encryption import writeFile, readFile, decrypt, encrypt
def testEncryption():
    # Read the key from the file named "key"
    key = readFile("key")
    # Encrypt the file named plainText
    ciphertext = encrypt('plainText', key)
    # Write contents of cipher to a file called 'cipherText' 
    writeFile('cipherText', ciphertext)
    # decrypt the file
    decrypted = decrypt(ciphertext, key)
    # Write the decrypted text to the file called plaintext1
    writeFile('plainText1', decrypted)

# call the function
testEncryption()
