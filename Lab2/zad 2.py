"""
Jan Wolski 2/26/24
Kodowanie za pomocą klucza i xor
"""

def encrypt(text, mask):
    text = [ord(a) for a in text]
    return ''.join([chr(a ^ mask) for a in text])


print(encrypt("Dupa", 0b11111))
