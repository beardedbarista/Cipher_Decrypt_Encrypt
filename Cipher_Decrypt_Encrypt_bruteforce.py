# Function to decrypt a Caesar cipher where the shift key is known
def decryption(cipher_text, key):
    plain_text = ""
    for char in cipher_text:
        if char.isalpha():  # Check if the character is a letter
            if char.islower():  # Check if the letter is lowercase
                decrypted_char = chr(((ord(char) - ord('a') + key ) % 26) + ord('a')) #decrypts the letters by adding the key from its ASCII adn wrapping around again with the modulos
            else:
                decrypted_char = chr(((ord(char) - ord('A') + key ) % 26) + ord('A'))
        else:
            decrypted_char = char  # If not a letter, keep it unchanged
        plain_text += decrypted_char
    return plain_text

# Input the key and cipher text. The below is a sample
key = 10 
cipher_text = "Xem Y myix, xem Y myix oek muhu xuhu. Mu'hu zkij jme beij iekbi, imyccydw yd q vyix remb Ouqh qvjuh ouqh, Hkddydw eluh jxu iqcu ebt whekdt, mxqj xqlu mu vekdt, Jxu iqcu ebt vuqhi, Myix oek muhu xuhu!" 

# Decrypt the ciphertext using the provided key
decrypted_char = decryption(cipher_text, key)
print("The decrypted message is: ", decrypted_char)


#Function to encrypt a Caeser Cipher where the shift key is known
def encryption (plain_text, key):
    cipher_text = ""
    for char in plain_text:
        if char.isalpha():  # Check if the character is a letter
            if char.islower():  # Check if the letter is lowercase
                encrypted_char = chr(((ord(char) - ord('a') - key ) % 26) + ord('a'))  #encrypts the letters by subtracting the key from its ASCII adn wrapping around again with the modulos
            else:
                encrypted_char = chr(((ord(char) - ord('A') - key ) % 26) + ord('A'))
        else:
            encrypted_char = char  # If not a letter, keep it unchanged
        cipher_text += encrypted_char
    return cipher_text

#Input the key and plain text. Call the function to encrypt the message by passing the 2 arguments and print the result
key = 10
plain_text = "How I wish, how I wish you were here. We're just two lost souls, swimming in a fish bowl Year after year, Running over the same old ground, what have we found, The same old fears, Wish you were here"
encrypted_char = encryption (plain_text, key)
print( "The encrypted message is: ", encrypted_char)


#Brute force function that iterates over each possibility
def brute_force_decryption(cipher_text):
    decrypt_result = []
    for key in range (26):
        plain_text = ""
        for char in cipher_text:
            if char.isalpha():  # Check if the character is a letter
                if char.islower():  # Check if the letter is lowercase
                    decrypted_char = chr(((ord(char) - ord('a') + key) % 26) + ord('a')) #decrypts the letters by adding the key from its ASCII adn wrapping around again with the modulos
                else:
                    decrypted_char = chr(((ord(char) - ord('A') + key) % 26) + ord('A'))
            else:
                decrypted_char = char  # If not a letter, keep it unchanged
            plain_text += decrypted_char
        decrypt_result.append(plain_text)
    return decrypt_result

cipher_text = " vhfinmxkl atox kxgwxkxw tee hy maxlx hew vbiaxkl hulhexmx. px'ee atox mh kxteer lmxi ni hnk ztfx by px ptgm mh dxxi hnk fxlltzxl ltyx."
decrypt_result = brute_force_decryption(cipher_text)
for key, decryped_text in enumerate(decrypt_result):
 print(key,decryped_text)