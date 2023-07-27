import os
from Cryptodome.Cipher import AES

def encrypt():
# set the key and IV (initialization vector)
 key = b'Sixteen byte key'
 iv = os.urandom(16)

# create the AES cipher object
 cipher = AES.new(key, AES.MODE_CBC, iv)

# open the input file for reading and the output file for writing
 with open('D:\\cloud\\Huffman-Coding\\videos\\video1.mp4.compressed', 'rb') as infile, open('encrypted_text_file.enc', 'wb') as outfile:
    # write the IV to the output file
    outfile.write(iv)

    # read the input file in blocks of 16 bytes and encrypt each block
    while True:
        plaintext = infile.read(16)
        if not plaintext:
            break
        # pad the last block if necessary
        if len(plaintext) % 16 != 0:
            plaintext += b' ' * (16 - len(plaintext) % 16)
        # encrypt the block
        ciphertext = cipher.encrypt(plaintext)
        # write the encrypted block to the output file
        outfile.write(ciphertext)