"""
Jand Wolski 2/26/24
"""
# zapis liczby
bin_num = 0b1101
oct_num = 0o1234
hex_num = 0x1FF

# konwersja liczby na łańcuch binarny
a = 10
print(bin(a))
print(oct(a))
print(hex(a))

# działania logiczne
a = 0b1010
b = 0b101

print(bin(a & b))  # AND
print(bin(a | b))  # OR
print(bin(a ^ b))  # XOR
print(bin(~a))     # NOT


# wypisanie wszystkich poteg 2
a = 0b1
for i in range(8):
    print(f"2 do {i} potęgi = {int(a)}")
    a= a<<1
