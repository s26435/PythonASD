import matplotlib.pyplot as plt
import random
import time

def binsearch(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid, arr[mid]
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1, None

# 1. Przykładowe wykorzystanie na 20 liczbach
numbers = [2, 4, 7, 10, 13, 15, 17, 19, 22, 25, 28, 31, 34, 37, 40, 43, 46, 49, 52, 55]
target = 31
position, value = binsearch(numbers, target)
if position != -1:
    print(f"Element {target} został znaleziony na pozycji {position} o wartości {value}.")
else:
    print(f"Element {target} nie został znaleziony.")

# 2. Funkcja binsearch na losowej liście
random_list = sorted(random.sample(range(1, 1000), 100))  # Losowa lista 100 elementów posortowana
print("Losowa lista:", random_list)
target = random.choice(random_list)  # Losowa liczba z listy
position, value = binsearch(random_list, target)
if position != -1:
    print(f"Element {target} został znaleziony na pozycji {position} o wartości {value}.")
else:
    print(f"Element {target} nie został znaleziony.")

# 3. Porównanie binsearch z przeszukiwaniem liniowym na dużych listach liczb całkowitych

binsearch_times = []
linear_search_times = []

for i in range(1000):  # Powtórzyć tysiąc razy
    numbers = random.sample(range(1, 1000000), i*1000)
    target = random.randint(1, 1000000)
    if(i%5==0):
        print(i)
    # Binsearch
    start_time = time.time()
    position, value = binsearch(numbers, target)
    end_time = time.time()
    binsearch_times.append(end_time - start_time)

    # Linear search
    start_time = time.time()
    if target in numbers:
        position = numbers.index(target)
    end_time = time.time()
    linear_search_times.append(end_time - start_time)

plt.plot(binsearch_times, label='Binsearch')
plt.plot(linear_search_times, label='Linear Search')
plt.xlabel('Iteration')
plt.ylabel('Time (seconds)')
plt.title('Comparison of Search Algorithms on Large Integer Lists')
plt.legend()
plt.savefig('search.jpg')

# 4. Porównanie binsearch z przeszukiwaniem liniowym na dużych listach liczb zmiennoprzecinkowych
# Zakładając, że lista liczb zmiennoprzecinkowych to 'random_float_list'

# 5. Porównanie binsearch z przeszukiwaniem liniowym na dużych listach liter
# Zakładając, że lista liter to 'random_char_list'
