"""
Jan Wolski 2/19/24
Program który po podaniu 3 liczb powie czy jest to trójak pitagoryjska
"""
def czy_trojka_pitagorejska(a, b, c):
    sorted_numbers = sorted([a, b, c])
    if sorted_numbers[0]**2 + sorted_numbers[1]**2 == sorted_numbers[2]**2:
        return True
    else:
        return False

a = int(input("Podaj pierwszą liczbę: "))
b = int(input("Podaj drugą liczbę: "))
c = int(input("Podaj trzecią liczbę: "))

if czy_trojka_pitagorejska(a, b, c):
    print(f"{a}, {b}, {c} to trójka pitagorejska.")
else:
    print(f"{a}, {b}, {c} to nie trójka pitagorejska.")
