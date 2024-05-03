import matplotlib.pyplot as plt
import time
import random
import string
import numpy as np


def wyszukiwanie_naiwne(matrix, text):
    indexes = []
    n = len(text)
    m = len(matrix)
    for i in range(n - m + 1):
        if text[i:i + m] == matrix:
            indexes.append(i)

    return indexes


def tablica_przesuniec(matrix):
    m = len(matrix)
    tablica = [0] * m
    d = 0

    for i in range(1, m):
        while d > 0 and matrix[d] != matrix[i]:
            d = tablica[d - 1]

        if matrix[d] == matrix[i]:
            d += 1

        tablica[i] = d
    return tablica


def wyszukiwanie_KMP(matrix, text):
    indexes = []
    n = len(text)
    m = len(matrix)
    table = tablica_przesuniec(matrix)
    q = 0

    for i in range(n):
        while q > 0 and matrix[q] != text[i]:
            q = table[q - 1]

        if matrix[q] == text[i]:
            q += 1

        if q == m:
            indexes.append(i - m + 1)
            q = table[q - 1]

    return indexes


def haszowanie(txt, m, d, q):
    h = 0
    for i in range(m):
        h = (d * h + ord(txt[i])) % q
    return h


def wyszukiwanie_KR(matrix, text, d=256, q=101):
    indexes = []
    n = len(text)
    m = len(matrix)

    wzorzec_hash = haszowanie(matrix, m, d, q)
    tekst_hash = haszowanie(text, m, d, q)

    for i in range(n - m + 1):
        if wzorzec_hash == tekst_hash:
            if text[i:i + m] == matrix:
                indexes.append(i)
        if i < n - m:
            tekst_hash = (d * (tekst_hash - ord(text[i]) * (d ** (m - 1))) + ord(text[i + m])) % q
            if tekst_hash < 0:
                tekst_hash = tekst_hash + q

    return indexes


def compare_functions(func, matrix, text):
    start_time = time.time()
    func(matrix, text)
    end_time = time.time()
    return end_time - start_time


def smooth_array(array, window_size=3):
    smoothed_array = []
    for i in range(len(array)):
        start_index = max(0, i - window_size // 2)
        end_index = min(len(array), i + window_size // 2 + 1)
        window = array[start_index:end_index]
        smoothed_value = sum(window) / len(window)
        smoothed_array.append(smoothed_value)
    return smoothed_array


if __name__ == "__main__":
    length = 300
    args = {wyszukiwanie_KR, wyszukiwanie_KMP, wyszukiwanie_naiwne}
    resultsKR = []
    resultsKMP = []
    resultsN = []
    lengthens = []

    for i in range(60):
        print(i)
        matrix = ''.join(random.choices(string.ascii_letters + string.digits, k=length))
        t = random.randint(0, length - 1)
        text = matrix[t:t + 3]
        lengthens.append(length)
        for x in args:
            t = compare_functions(x, text, matrix)
            if x == wyszukiwanie_KR:
                resultsKR.append(t)
            elif x == wyszukiwanie_KMP:
                resultsKMP.append(t)
            else:
                resultsN.append(t)

        length = int(length*1.2)

    plt.plot(lengthens, resultsKR, marker='', linestyle='-', color='g', label='KR')
    plt.plot(lengthens, resultsN, marker='', linestyle='-', color='r', label='naiwne')
    plt.plot(lengthens, resultsKMP, marker='', linestyle='-', color='r', label='KMP')
    plt.xlabel('Ilość elementów tablicy(w tys.)')
    plt.ylabel('Czas(s)')
    plt.title('Porównanie czasu wykonania algorytmów wyszukiwania')
    plt.legend()
    plt.savefig("compare.jpg")
