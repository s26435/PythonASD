import math
from math import nan
import sys

def funkcja1(x):
    return math.sin(pow(x,2)- x + (1/3)) + x/2

def miejsceZerowe(funkcja, a, b, epsilon):
    if a >= b:
        print("Przediał nie może zaczynać się od wiekszej liczby niż sie kończy!", file=sys.stderr)
        return nan

    ya = funkcja(a)
    yb = funkcja(b)

    if ya*yb >= 0:
        print("W podanym przedizale musi istnieć miejsce zerowe!", file=sys.stderr)
        return nan

    while True:
        x = (a + b) / 2
        y = funkcja(x)
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







if __name__ == "__main__":
    print(miejsceZerowe(funkcja1, -10, 10, 1e-10))