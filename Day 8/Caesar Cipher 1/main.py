alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
# text = input("Type your message:\n").lower()
# shift = int(input("Type the shift number:\n"))


# TODO-1: Create a function called 'encrypt()' that takes 'original_text' and 'shift_amount' as 2 inputs.

def encrypt_decrypt(orig_text, shift_num, encode_decode):
    cipher_mssg=""
    if encode_decode=="decode":
        shift_num *=-1
    
        
    for letter in orig_text:
        if letter not in alphabet:
            cipher_mssg += letter
        else:
            shifted_letter_pos=alphabet.index(letter)+shift_num
            shifted_letter_pos %= len(alphabet)
            cipher_mssg += alphabet[shifted_letter_pos]
    print(f"encrypted/decrypted  message is: {cipher_mssg}")
    
should_continue=True

while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    encrypt_decrypt(text, shift, direction)
    
    restart=input("Do you want to contue? Press Y to continue and press N to exit: ").lower()
    if restart != "y" and restart != "n":
       print("Invalid entry")
    elif restart == "n":
        should_continue=False
        print("Goodbye")


