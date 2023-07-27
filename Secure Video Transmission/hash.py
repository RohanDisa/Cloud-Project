import hashlib
from Cryptodome.Cipher import AES

def hashing():
# Read the encrypted file
 print("Hashing the file...")
# Read the encrypted file
 with open("D:/cloud/Huffman-Coding/encrypted_text_file.enc", "rb") as f:
    encrypted_data = f.read()

# Hash the encrypted data using SHA256 hash function
 hash_object = hashlib.sha256(encrypted_data)
 hex_dig = hash_object.hexdigest()
 with open("hash.txt", "w") as f:
    f.write(hex_dig)
 print("Successfully hashed")
#hashing()

def hashVerification():
 
# filename = 'D:/cloud/Huffman-Coding/encrypted_text_file.enc'
 hash_filename = 'D:\\cloud\\Huffman-Coding\\hash.txt'

# Read the hash from the hash file
 with open(hash_filename, 'rb') as f:
    original_hash = f.read()
 
 original_hash = original_hash.decode('utf-8')


 with open("D:/cloud/downloadedfile.enc", "rb") as f:
    encrypted_data = f.read()

# Hash the encrypted data using SHA256 hash function
 hash_object = hashlib.sha256(encrypted_data)
 hex_dig = hash_object.hexdigest()


 if hex_dig == original_hash:
    print('The file has not been modified.')
 else:
    print('The file has been modified.')
#hashVerification()
