"""
Jan Wolski 2/26/24
Kodowanie za pomocą klucza i xor
"""


def encrypt(text, mask):  # funkcja
    text = [ord(a) for a in text]  # tworzenie tablicy liczb która kazda z nich jest ascc kolejnych liter w tekscie
    return ''.join([chr(a ^ mask) for a in text])  # szyfrowanie maską i zamienianie spowrotem na litery


# wykorzystanie
zaszyfrowane = encrypt("Tak", 0b1000)
print(f"Zaszyfrowane: {zaszyfrowane}")
deszyfrowane = encrypt(zaszyfrowane, 0b1000)
print(f"Deszyfrowane: {deszyfrowane}")

print(pow(2, 3))