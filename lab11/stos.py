class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            raise IndexError("Stack is empty")

    def is_empty(self):
        return len(self.items) == 0


def czy_nawiasy_sa_poprawne(ciag):
    stos = Stack()
    pary_nawiasow = {')': '(', ']': '[', '}': '{'}

    for znak in ciag:
        if znak in pary_nawiasow.values():
            stos.push(znak)
        elif znak in pary_nawiasow.keys():
            if not stos.is_empty() and stos.pop() == pary_nawiasow[znak]:
                continue
            else:
                return False

    return stos.is_empty()


def evaluate_expression(expression):
    stack = Stack()
    operators = {'+', '-', '*', '/'}

    for token in expression:
        if token not in operators:
            stack.push(float(token))
        else:
            if len(stack.items) < 2:
                raise ValueError("Źle napisane wyrażenie.")

            num2 = stack.pop()
            num1 = stack.pop()

            if token == '+':
                result = num1 + num2
            elif token == '-':
                result = num1 - num2
            elif token == '*':
                result = num1 * num2
            elif token == '/':
                if num2 == 0:
                    raise ValueError("Dzielenie przez zero")
                result = num1 / num2

            stack.push(result)

    if len(stack.items) == 1:
        return stack.pop()
    else:
        raise ValueError("Źle napisane wyrażenie.")

def main():
    expression = input("Podaj wyrażenie w odwrotnej notacji polskiej (oddzielając liczby i operatory spacją): ")
    tokens = expression.split()
    try:
        result = evaluate_expression(tokens)
        print("Wynik:", result)
    except (ValueError, IndexError) as e:
        print("Błąd:", e)

    ciag1 = "{[()()]}"
    print(czy_nawiasy_sa_poprawne(ciag1))

    ciag2 = "{[(])}"
    print(czy_nawiasy_sa_poprawne(ciag2))

if __name__ == "__main__":
    main()
