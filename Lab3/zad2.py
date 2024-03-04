from zad1 import miejsceZerowe, funkcja1
from math import cos
def f1(x):
    return funkcja1(x)

def f2(x):
    return pow(x,3)-3*pow(x,2)+2*x - 5

def f3(x):
    return cos(x)-1

if __name__ == "__main__":
    a = -3
    b = 0
    epsilon = 1e-10
    print("x0 funkcji f1 to:", miejsceZerowe(f1, a, b, epsilon))
    print("x0 funkcji f2 to:", miejsceZerowe(f2, a, b, epsilon))
    print("x0 funkcji f3 to:", miejsceZerowe(f3, a, b, epsilon))