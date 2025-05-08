# Function to encrypt the string using Caesar Cipher
def encrypt_string(plain_text, shift):
    encrypted_text = ""
    for char in plain_text:
        if char.isalpha():  # Encrypt only alphabetic characters
            shift_base = 65 if char.isupper() else 97  # 'A' = 65, 'a' = 97
            encrypted_text += chr((ord(char) + shift - shift_base) % 26 + shift_base)
        else:
            encrypted_text += char  # Non-alphabetic characters remain unchanged
    return encrypted_text

# Function to decrypt the string using Caesar Cipher
def decrypt_string(encrypted_text, shift):
    decrypted_text = ""
    for char in encrypted_text:
        if char.isalpha():  # Decrypt only alphabetic characters
            shift_base = 65 if char.isupper() else 97  # 'A' = 65, 'a' = 97
            decrypted_text += chr((ord(char) - shift - shift_base) % 26 + shift_base)
        else:
            decrypted_text += char  # Non-alphabetic characters remain unchanged
    return decrypted_text

# Example usage
# if __name__ == "__main__":
shift_value = int(input("give the shift of encryption"))  # Number of positions to shift
text_to_encrypt = input("give text")  # Example input text

    # Encrypt the string
encrypted_text = encrypt_string(text_to_encrypt, shift_value)
print(f"Encrypted Text: {encrypted_text}")

    # Decrypt the string
    decrypted_text = decrypt_string(encrypted_text, shift_value)
    print(f"Decrypted Text: {decrypted_text}")
