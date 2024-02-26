"""
Jan Wolski 2/9/24
Zliczanie częstości występowania liter w file.txt
i przedstawianie go na wykresie słupkowym.
"""

import matplotlib.pyplot as plt

with open("file.txt") as file:
    content = file.read()

counter = {}

for letter in content:
    if letter.isalpha():
        letter = letter.lower()
        if letter in counter:
            counter[letter] += 1
        else:
            counter[letter] = 1

print(counter)
names = list(counter.keys())
values = list(counter.values())

plt.bar(range(len(counter)), values, tick_label=names)
plt.savefig("a.jpg")
