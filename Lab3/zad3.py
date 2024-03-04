"""
Tak naprawde to zadanie 4 z kartki

"""

from zad1 import miejsceZerowe
from math import cos, sin
import math

def sinMinusCos(x):
    return sin(x) - cos(x)


a = 0
b = math.pi

print(f"Miejsce przecięcia funkcji sinus i cosinus w przedziale <{a},{b:.2f}> to: ", miejsceZerowe(sinMinusCos, a,b , 1e-10))
