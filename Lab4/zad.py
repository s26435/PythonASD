import time, random
import matplotlib.pyplot as plt


def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j

        arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr


def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]
        merge_sort(left_half)
        merge_sort(right_half)
        i, j, k = 0, 0, 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

    return arr


def take(fun, size):
    arr = [random.randint(1, 1000) for _ in range(size)]
    start_time = time.time()
    fun(arr.copy())
    fun_time = time.time() - start_time
    return fun_time


if __name__ == "__main__":
    dict_buble = {}
    dict_merge = {}
    dict_sel = {}
    dic_sort = {}
    for i in range(40):
        dict_buble[i+1] = take(bubble_sort, i*1000)
        dict_merge[i + 1] = take(merge_sort, i * 1000)
        dict_sel[i+1] = take(selection_sort, i * 1000)
        dic_sort[i + 1] = take(sorted, i * 1000)
        print(i + 1)

    values = list(dict_buble.values())
    plt.plot(range(len(dict_buble)), values, marker='o', linestyle='-', color='b', label='bublesort')
    plt.xlabel('Ilość elementów tablicy(w tys.)')
    plt.ylabel('Czas(s)')
    values = list(dict_merge.values())
    plt.plot(range(len(dict_merge)), values, marker='o', linestyle='-', color='r', label='mergesort')
    plt.xlabel('Ilość elementów tablicy(w tys.)')
    plt.ylabel('Czas(s)')
    values = list(dict_sel.values())
    plt.plot(range(len(dict_sel)), values, marker='o', linestyle='-', color='y', label='selection sort')
    plt.xlabel('Ilość elementów tablicy(w tys.)')
    plt.ylabel('Czas(s)')
    plt.title('Wykres dla sortowanie przez selekcję')
    values = list(dic_sort.values())
    plt.plot(range(len(dic_sort)), values, marker='o', linestyle='-', color='g', label='funkcja \'sorted\'')
    plt.xlabel('Ilość elementów tablicy(w tys.)')
    plt.ylabel('Czas(s)')
    plt.title('Porównanie czasu wykonania algorytmów sortujących')
    plt.legend()
    plt.savefig("compare.jpg")
