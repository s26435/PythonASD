"""

"""
import random
import time
import matplotlib.pyplot as plt

def smooth_array(arr):
    smoothed_arr = []
    for i in range(len(arr)):
        if i == 0 or i == len(arr) - 1:
            smoothed_arr.append(arr[i])  # Zachowaj pierwszy i ostatni element niezmieniony
        else:
            smoothed_value = (arr[i - 1] + arr[i] + arr[i + 1]) / 3  # Uśrednianie trzech sąsiednich elementów
            smoothed_arr.append(smoothed_value)
    return smoothed_arr


def take_time_random(fun, size):
    target = random.randint(1, 1000000)
    arr = [random.randint(1, 1000000) for _ in range(size)]
    start_time = time.time()
    fun(target, arr.copy())
    fun_time = time.time() - start_time
    return fun_time


def linear_search(target, tab):
    for i in range(len(tab)):
        if tab[i] == target:
            return i
    return -1


def binsearch(target, tab):
    start = 0
    end = len(tab) - 1
    while start <= end:
        mid = (start + end) // 2
        if target < tab[mid]:
            end = mid - 1
        elif target > tab[mid]:
            start = mid + 1
        else:
            return mid
    return -1

bins = []
lin = []

for i in range(1000, 1000000, 1000):
    bins.append(take_time_random(binsearch, i))
    lin.append(take_time_random(linear_search, i))
    print(f'{i},')




plt.plot(range(len(bins)), smooth_array(bins), marker='', linestyle='-', color='g', label='szukanie binarne:')
plt.plot(range(len(lin)), smooth_array(lin), marker='', linestyle='-', color='r', label='szukanie liniowe:')
plt.xlabel('Ilość elementów tablicy(w tys.)')
plt.ylabel('Czas(s)')
plt.title('Porównanie czasu wykonania algorytmów wyszukiwania')
plt.legend()
plt.savefig("compare.jpg")
