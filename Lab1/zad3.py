"""
Jan Wolski 2/9/24
Obliczanie wielkości populacji na podstawie ilości dni
i procentowego przyrostu.
"""
poczatkowa = int(input("Podaj początkową liczbę organizmów: "))
dzienny_przyrost = int(input("Podaj przyrost dzienny(w procętach): "))/100
dni = int(input("Podaj ilość dni "))

for i in range(dni):
    poczatkowa += poczatkowa*dzienny_przyrost
    print(f"Dzień {i+1}: {poczatkowa:.3f}")
