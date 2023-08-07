
def caesar_cipher(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            ascii_offset = ord('a') if char.islower() else ord('A')
            shifted_char = chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)
            encrypted_text += shifted_char
        else:
            encrypted_text += char
    return encrypted_text

def main():
    plain_text = input("Enter a plain text: ")
    encrypted_text = caesar_cipher(plain_text, 5)
    print("Encrypted text:", encrypted_text)

if __name__ == "__main__":
    main()
