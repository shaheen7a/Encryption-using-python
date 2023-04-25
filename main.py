from cryptography.fernet import Fernet


#------------------------------------
# Create the key

# key = Fernet.generate_key()

# with open('enc_key.key', 'wb') as enc_key:
#     enc_key.write(key)

#------------------------------------
#Load the key

with open('enc_key.key', 'rb') as enc_key:
    key = enc_key.read()

print(key)

#------------------------------------
#encryption

# f = Fernet(key)

# with open('personal_data.csv', 'rb') as original_file:
#     original = original_file.read()

# encrypted = f.encrypt(original)

# with open ('enc_personal_data.csv', 'wb') as encrypted_file:
#     encrypted_file.write(encrypted)

#------------------------------------
#Decryption

f = Fernet(key)

with open('enc_personal_data.csv', 'rb') as encrypted_file:
    encrypted = encrypted_file.read()

decrypted = f.decrypt(encrypted)

with open('dec_personal_data.csv', 'wb') as decrypted_file:
    decrypted_file.write(decrypted)

