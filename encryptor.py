from main import Pytanie
import random as rnd

mask = 10

def unidecode(tekst):
    zamiany = {
        'ą': 'a', 'ć': 'c', 'ę': 'e', 'ł': 'l', 'ń': 'n',
        'ó': 'o', 'ś': 's', 'ź': 'z', 'ż': 'z',
        'Ą': 'A', 'Ć': 'C', 'Ę': 'E', 'Ł': 'L', 'Ń': 'N',
        'Ó': 'O', 'Ś': 'S', 'Ź': 'Z', 'Ż': 'Z'
    }
    return ''.join(zamiany.get(znak, znak) for znak in tekst)

def encrypt(text, mask):
    text = [ord(a) for a in text]
    return ''.join([chr(a + mask) for a in text])


content = []
try:
    with open("text.txt", 'r') as file:
        for line in file:
            print(line)
            content.append(line.replace('\n', ''))

    tabOfQuestions = []
    for i in range(int(len(content) / 6)):
        index = i * 6
        tabOfQuestions.append(
            Pytanie(i, unidecode(content[index]), unidecode(content[index + 1]), unidecode(content[index + 2]),
                    unidecode(content[index + 3]), unidecode(content[index + 4]), unidecode(content[index + 5])))
except Exception as e:
    print(e)

for i in tabOfQuestions:
    i.poprawnaodp = encrypt(i.poprawnaodp, mask)
    i.print()

with open("text.txt", 'w') as file:
    for q in tabOfQuestions:
        file.write(q.toString() + chr(rnd.randint(65, 90)) + '\n')
