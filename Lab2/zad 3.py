"""
Jan Wolski 2/26/24
"""


def contains(text, mask):
    true = ''
    mask = bin(mask)[2:]
    for i in range(len(text) - len(mask)):
        true += "0"
    mask = true + mask
    # zamiana maski bitowej na tekst
    tab = []  # inicjalizowanie pustej tablicy (aby dodawać do niej nowe znaki)
    for i in range(len(text)):  # iterowanie po kazdej literze w tekscie
        if mask[i] == '1':  # jesli odpowiadający bit w masce jest równy jeden to dodajemy do tablicy
            tab.append(text[i])
    return ''.join(tab)  # zwracamy tablicę zamienioną na string





def looping(text):
    dict = {}
    text = text.replace(' ', '').lower()  # usuwanie spacji i dużych liter
    count = 0

    for i in range(pow(2, len(text))):  # generowanie kluczy od 1-d 2 do potęgi długość tekstu
        temp = contains(text[::-1], i)[::-1]
        # print(f"nr.{i}={temp}")  # sprawdzanie klucza dla kazdego z kluczy
        if not temp in dict:
            dict[temp] = 1
        else:
            dict[temp] = dict.get(temp)+1
            count += 1
    return dict


print(looping("boażena").keys())

