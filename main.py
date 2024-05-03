mask = 10

class Pytanie:
    def __init__(self, id, tresc, odpA, odpB, odpC, odpD, poprawnaodp):
        self.id = id
        self.tresc = tresc
        self.odpA = odpA
        self.odpB = odpB
        self.odpC = odpC
        self.odpD = odpD
        self.poprawnaodp = poprawnaodp

    def decrypt(self, mask):
        self.poprawnaodp = chr(ord(self.poprawnaodp[0]) - mask)

    def print(self):
        print("----------------------")
        print(self.tresc)
        print("----------------------")
        print(f"A) {self.odpA}")
        print(f"B) {self.odpB}")
        print(f"C) {self.odpC}")
        print(f"D) {self.odpD}")

    def toString(self):
        return ''.join(self.tresc + '\n' + self.odpA + '\n' + self.odpB + '\n' + self.odpC + '\n' + self.odpD + '\n' + self.poprawnaodp)

class GameLoop:
    def __init__(self):
        content = []
        with open("text.txt") as file:
            for line in file:
                content.append(line.replace('\n', ''))

        print(len(content) / 6)
        tabOfQuestions = []
        try:
            for i in range(int(len(content) / 6)):
                index = i * 6
                temp = Pytanie(i, content[index], content[index + 1], content[index + 2], content[index + 3],
                               content[index + 4], content[index + 5])
                temp.decrypt(mask)
                tabOfQuestions.append(temp)
        except Exception as message:
            print(message)
        except:
            pass

        self.questions = tabOfQuestions
        self.score = 0

    def start(self):
        self.score = 0
        for question in self.questions:
            question.print()
            if input("Podaj poprawną odpowiedz: ").lower() == question.poprawnaodp:
                print("Poprawna odpowiedź!")
                self.score += 1
            else:
                print(f"Niepoprawna odpowiedź\n poprawna odpowiedź to: {question.poprawnaodp}")

            print(f"Wynik: {self.score}")


if __name__ == '__main__':
    gameLoop = GameLoop()
    gameLoop.start()
    input("Naciśnij dowolny przycisk aby zakończyć...")