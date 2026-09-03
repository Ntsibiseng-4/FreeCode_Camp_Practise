"""
alphabet = 'abcdefghijklmnopqrstuvwxyz'       #Original: abcdefghijklmnopqrstuvwxyz
shift = 5
shifted_alphabet = alphabet[shift:] + alphabet[:shift]  #Shifted:  fghijklmnopqrstuvwxyzabcde
translation_table = str.maketrans(alphabet, shifted_alphabet)
#text = 'hello world'
#encrypted_text = text.translate(translation_table)
print(encrypted_text)     h → m, e → j, l → q, l → q, o → t,  message has been encrypted
"""

def caesar(text, shift, encrypt=True):

    if not isinstance(shift, int):
        return 'Shift must be an integer value.'

    if shift < 1 or shift > 25:
        return 'Shift must be an integer between 1 and 25.'

    alphabet = 'abcdefghijklmnopqrstuvwxyz'

    if not encrypt:
        shift = - shift   #shift becomes negative
    
    shifted_alphabet = alphabet[shift:] + alphabet[:shift]
    translation_table = str.maketrans(alphabet + alphabet.upper(), shifted_alphabet + shifted_alphabet.upper())
    encrypted_text = text.translate(translation_table)
    return encrypted_text

def encrypt(text, shift):   #Encryption → move letters forward
    return caesar(text, shift)   
    
def decrypt(text, shift):    #Decryption → move letters backward
    return caesar(text, shift, encrypt=False)

encrypted_text = "Pbhentr vf sbhaq va hayvxryl cynprf."
print(encrypted_text)
decrypted_text = decrypt(encrypted_text, 13)
print(decrypted_text)