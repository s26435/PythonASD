"""
Jan Wolski 2/26/24
Przedstawienie liczb binarnych, ósemkowych i szesnatkowych oraz
operatorów bitowych.
"""
# zapis liczby
bin_num = 0b1101 # binarna
oct_num = 0o1234 # ósemkowa
hex_num = 0x1FF # szesnastkowa

# konwersja liczby na łańcuch binarny
a = 10
print(bin(a)) # dec -> binarna
print(oct(a)) # dec -> óemkowa
print(hex(a)) # dec -> szesnastkowa

# działania logiczne
a = 0b1010
b = 0b101

print(bin(a & b))  # AND iloczyn logiczny
print(bin(a | b))  # OR suma logiczna
print(bin(a ^ b))  # XOR alternatywa rozłączna
print(bin(~a))     # NOT zaprzeczenie


# wypisanie wszystkich poteg 2
a = 0b1 # liczba binarna 1
for i in range(8): #iterowanie tyle razy ile chcemy potęg
    print(f"2 do {i} potęgi = {int(a)}") # wypisywanie potęgi
    a= a<<1 # przesówanie bitu w lewo
