import string

with open('cipher.txt') as f:
    cipher = f.read()

alphabet = string.ascii_uppercase

def encrypt(plain_text, key):
    encryption_key = ""
    i = 0
    while len(encryption_key) < len(plain_text):
        encryption_key += key[i]
        i += 1
        if i >= len(key):
            i = 0

    letter_indexes = []
    for letter_1, letter_2 in zip(list(plain_text), list(encryption_key)):
        letter_1_index = alphabet.index(letter_1.upper())
        letter_2_index = alphabet.index(letter_2.upper())
        letter_indexes.append((letter_1_index + letter_2_index) % 26)

    encrypted_msg = ""
    for index in letter_indexes:
        encrypted_msg += alphabet[index]

    return encrypted_msg


def decrypt(encrypted_text, key):
    alpha_chars = []
    alpha_indexes = []
    for i, letter in enumerate(list(encrypted_text)):
        if letter.isalpha():
            alpha_chars.append(letter)
            alpha_indexes.append(i)

    encryption_key = ""
    i = 0
    while len(encryption_key) < len(alpha_chars):
        encryption_key += key[i]
        i += 1
        if i >= len(key):
            i = 0

    letter_indexes = []
    for letter_1, letter_2 in zip(list(alpha_chars), list(encryption_key)):
        letter_1_index = alphabet.index(letter_1.upper())
        letter_2_index = alphabet.index(letter_2.upper())
        letter_indexes.append((letter_1_index - letter_2_index) % 26)

    letters = [alphabet[i] for i in letter_indexes]

    decrypted_text = list(encrypted_text)
    for index, letter in zip(alpha_indexes, letters):
        decrypted_text[index] = letter

    decrypted_msg = "".join(str(letter) for letter in decrypted_text)
    return decrypted_msg

# Key is CYLAB
print(decrypt(cipher, "CYLAB"))
