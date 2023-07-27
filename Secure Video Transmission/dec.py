import os
from Cryptodome.Cipher import AES
from Cryptodome.Util.Padding import unpad

def decrypt():
    # Set the key and IV
    key = b'Sixteen byte key'

    # Create the AES cipher object
    cipher = AES.new(key, AES.MODE_CBC)

    # Open the input file for reading and the output file for writing
    with open('D:\\cloud\\Huffman-Coding\\encrypted_text_file.enc', 'rb') as infile, open('decrypted_text_file.txt', 'wb') as outfile:
        # Read the IV from the input file
        iv = infile.read(16)
        cipher = AES.new(key, AES.MODE_CBC, iv)

        # Read the input file in blocks of 16 bytes and decrypt each block
        while True:
            ciphertext = infile.read(16)
            if not ciphertext:
                break
            # Decrypt the block
            plaintext = cipher.decrypt(ciphertext)
            # Write the decrypted block to the output file
            outfile.write(plaintext)

    # Remove the padding from the decrypted data
    with open('decrypted_text_file.txt', 'rb+') as outfile:
        # Get the file size
        file_size = os.path.getsize('decrypted_text_file.txt')
        if file_size > 0:
            # Calculate the padding length
            padding_length = outfile.read()[-1]
            # Truncate the file to remove the padding
            outfile.truncate(file_size - padding_length)

# Call the decrypt function
#decrypt()
