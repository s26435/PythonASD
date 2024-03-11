"""
zadanie 5 z kartki
"""
from math import nan
import sys
def pierwiastek_liczby(a, n):
    return pow(a, 2) - n



def miejsceZerowe(funkcja, a, b, n, epsilon):
    if a >= b:
        print("Przediał nie może zaczynać się od wiekszej liczby niż sie kończy!", file=sys.stderr)
        return nan

    ya = funkcja(a, n)
    yb = funkcja(b, n)

    if ya*yb >= 0:
        print("W podanym przedizale musi istnieć miejsce zerowe!", file=sys.stderr)
        return nan

    while True:
        x = (a + b) / 2
        y = funkcja(x, n)
        if ya * y < 0:
            b = x
        else:
            a = x
            ya = y
        if abs(b-a) < epsilon:
            break
        if y == 0:
            break
    return x

n = 9
print(miejsceZerowe(pierwiastek_liczby, 0, 5, n, 1e-10))