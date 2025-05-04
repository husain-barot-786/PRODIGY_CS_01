# Caesar Cipher Program

def encrypt_caesar(plaintext, shift):
    """
    Encrypts the given plaintext using Caesar Cipher.
    
    Parameters:
    - plaintext (str): The message to encrypt.
    - shift (int): Number of positions to shift.
    
    Returns:
    - str: Encrypted ciphertext.
    """
    ciphertext = ""
    
    for char in plaintext:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            shifted_char = chr((ord(char) - base + shift) % 26 + base)
            ciphertext += shifted_char
        else:
            ciphertext += char  # Keep punctuation, digits, etc. unchanged
    return ciphertext

def decrypt_caesar(ciphertext, shift):
    """
    Decrypts the given ciphertext using Caesar Cipher.
    
    Parameters:
    - ciphertext (str): The encrypted message.
    - shift (int): Number of positions to shift back.
    
    Returns:
    - str: Decrypted original text.
    """
    return encrypt_caesar(ciphertext, -shift)  # Reverse the shift for decryption

def main():
    print("==== Caesar Cipher Encryption & Decryption ====")
    
    # User input
    message = input("Enter the message: ")
    while True:
        try:
            shift = int(input("Enter the shift value (integer): "))
            break
        except ValueError:
            print("Invalid input! Please enter a valid integer for shift.")
    
    print("\n--- Encryption ---")
    encrypted_text = encrypt_caesar(message, shift)
    print("Encrypted Message:", encrypted_text)

    print("\n--- Decryption ---")
    decrypted_text = decrypt_caesar(encrypted_text, shift)
    print("Decrypted Message:", decrypted_text)

if __name__ == "__main__":
    main()
