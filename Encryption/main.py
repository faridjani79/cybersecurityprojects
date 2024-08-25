from cryptography.fernet import Fernet

# Generate a key
key = Fernet.generate_key()

#Saving the encryption key in a file
with open('mykey.key', 'wb') as mykey:
  mykey.write(key)

#Load the encryption key / can be used to run the decryption when the encrypted file has been generated
with open("mykey.key", "rb") as mykey:
  key = mykey.read()

""" It is not advisable to print the key from security perspective however in this code,just want to make sure the key is there"""
print(key)

# Encrypt the file

f = Fernet(key)

student_list = "c:\\Users\\user\\Desktop\\Python courses\\Cryptography Project\\List of student.txt" #Path where the original file located

with open(student_list, "rb")as original_file:
    original = original_file.read()

# Encrypt the data
encrypted = f.encrypt(original)

# Write the encryption data and key into a file
with open ("enc_student_list.txt", "wb") as encrypted_file:
    encrypted_file.write(encrypted)

# Create key (the same key)

f = Fernet(key)

# Load the encryption file
with open("enc_student_list.txt", "rb") as encrypted_file:
    encrypted = encrypted_file.read()

# Decrypt the file
decrypted = f.decrypt(encrypted)

#Write the encryption file
with open("dec_student_list.txt", "wb") as decrypted_file:
    decrypted_file.write(decrypted)

print(" Decryption is successfull")