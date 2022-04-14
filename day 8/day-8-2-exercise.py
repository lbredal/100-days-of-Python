# File includes part 2 and 3 of today's exercise

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


def encrypt(plain_text, shift_amount):
    cipher_text = ""
    for letter in plain_text:
        position = alphabet.index(letter)
        new_position = position + shift_amount
        if (new_position > len(alphabet)):
            new_position = new_position - len(alphabet)
        cipher_text += alphabet[new_position]
    print(f"The encoded text is {cipher_text}")

def decrypt(cipher_text, shift_amount):
    plain_text = ""
    for letter in cipher_text:
        position = alphabet.index(letter)
        new_position = position - shift_amount
        if (new_position < 1):
            new_position = new_position + len(alphabet)
        plain_text +=  alphabet[new_position]
    print(f"The decoded text is {plain_text}")

def caesar(text, shift, direction):
    caesar_text = ""
    for letter in text:
        position = alphabet.index(letter)
        if direction == "encode":
            new_position = position + shift
            if (new_position > len(alphabet)):
                new_position = new_position - len(alphabet)
            caesar_text += alphabet[new_position]
        elif direction == "decode":
            new_position = position - shift
            if (new_position < 1):
                new_position = new_position + len(alphabet)
            caesar_text +=  alphabet[new_position]
    print(f"The text is {caesar_text}")            

    

   
caesar(text, shift, direction)