"""
Jan Wolski 2/26/24
Kodowanie za pomocą klucza i xor
"""


def text_to_ascii(text):
    ascii = [ord(a) for a in text]
    return ascii


def ascii_to_text(table):
    return ''.join(chr(num) for num in table)

def encrypt(text, mask):
    text = text_to_ascii(text)
    return ascii_to_text([a ^ mask for a in text])


print(encrypt("Dupa", 0b11111))
