"""
Jan Wolski 2/9/24
Gra w zgadywanie. program losuje jedną liczbę 1-100.
a gracz zgaduje tą liczbę a program go informuje czy jest mniejsza czy wieksza.
"""

import random as rn

x = rn.randint(1, 100)
i = 0
print("Pomyślałem o liczbie od 1 do 100")
while True:
    guess = int(input("Podaj liczbę od 1 do 100: "))
    if guess < x:
        print(f"{guess} jest za mała!")
        i += 1
    elif guess > x:
        print(f"{guess} jest za duża!")
        i += 1
    else:
        print(f"Zgadłeś!!!\n Potrzebowałeś na to {i} prób!")
        break
