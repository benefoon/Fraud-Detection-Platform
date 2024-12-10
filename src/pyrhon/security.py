from cryptography.fernet import Fernet

# Generate encryption key
def generate_key():
    return Fernet.generate_key()

# Encrypt sensitive data
def encrypt_data(data, key):
    cipher = Fernet(key)
    encrypted_data = cipher.encrypt(data.encode())
    return encrypted_data

# Decrypt sensitive data
def decrypt_data(encrypted_data, key):
    cipher = Fernet(key)
    decrypted_data = cipher.decrypt(encrypted_data).decode()
    return decrypted_data
