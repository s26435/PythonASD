poczatkowa = int(input("Podaj początkową liczbę organizmów: "))
dzienny_przyrost = int(input("Podaj przyrost dzienny(w procętach): "))/100
dni = int(input("Podaj ilość dni "))

for i in range(dni):
    poczatkowa += poczatkowa*dzienny_przyrost
    print(f"Dzień {i}: {poczatkowa:.3f}")