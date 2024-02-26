"""
Jan Wolski 2/26/24
Zamiana liczby binarnej na dziesiętną
"""
# string liczby do zamienienia z binarnej na decymalną
num = "11"

x = 0

# iteracja po każdej cyfsze binarnej
for i in range(len(num)):
    x += int(num[i]) * (pow(2, len(num) - i - 1)) # dodawanie do liczby potęge liczby dwa

print(x)
