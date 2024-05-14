import turtle


def draw_tree(t, branch_length, angle, depth):
    if depth > 0:
        t.forward(branch_length)
        t.left(angle)
        draw_tree(t, branch_length * 0.7, angle, depth - 1)
        t.right(2 * angle)
        draw_tree(t, branch_length * 0.7, angle, depth - 1)
        t.left(angle)
        t.backward(branch_length)


def draw_sierpinski_carpet(t, depth, size):
    if depth == 0:
        t.begin_fill()
        for _ in range(4):
            t.forward(size)
            t.left(90)
        t.end_fill()
    else:
        new_size = size / 3
        for i in range(3):
            for j in range(3):
                t.penup()
                t.goto(t.xcor() + new_size * j, t.ycor() - new_size * i)
                if i != 1 or j != 1:
                    t.pendown()
                    draw_sierpinski_carpet(t, depth - 1, new_size)


def draw_koch_curve(t, length, depth):
    if depth == 0:
        t.forward(length)
    else:
        length /= 3.0
        draw_koch_curve(t, length, depth - 1)
        t.left(60)
        draw_koch_curve(t, length, depth - 1)
        t.right(120)
        draw_koch_curve(t, length, depth - 1)
        t.left(60)
        draw_koch_curve(t, length, depth - 1)


def draw_koch_snowflake(t, length, depth):
    for _ in range(3):
        draw_koch_curve(t, length, depth)
        t.right(120)


def draw_sierpinski_triangle(t, length, depth):
    if depth == 0:
        for _ in range(3):
            t.forward(length)
            t.left(120)
    else:
        length /= 2
        draw_sierpinski_triangle(t, length, depth - 1)
        t.forward(length)
        draw_sierpinski_triangle(t, length, depth - 1)
        t.backward(length)
        t.left(60)
        t.forward(length)
        t.right(60)
        draw_sierpinski_triangle(t, length, depth - 1)
        t.left(60)
        t.backward(length)
        t.right(60)


def clear_screen(t):
    t.clear()
    t.penup()
    t.home()
    t.pendown()


def main():
    screen = turtle.Screen()
    screen.bgcolor("white")
    t = turtle.Turtle()
    t.speed(0)

    while True:
        print("Wybierz fraktal do narysowania:")
        print("1. Drzewo binarne")
        print("2. Dywan Sierpińskiego")
        print("3. Płatek von Kocha")
        print("4. Trójkąt Sierpińskiego")
        print("5. Wyczyść ekran")
        print("6. Zakończ program")

        choice = int(input("Podaj numer wyboru: "))

        if choice == 1:
            clear_screen(t)
            t.left(90)
            t.penup()
            t.goto(0, -250)
            t.pendown()
            draw_tree(t, 100, 30, 6)
        elif choice == 2:
            clear_screen(t)
            t.penup()
            t.goto(-200, 200)
            t.pendown()
            t.color("black", "white")
            t.begin_fill()
            for _ in range(4):
                t.forward(600)
                t.right(90)
            t.end_fill()
            t.color("black", "black")
            draw_sierpinski_carpet(t, 4, 200)
        elif choice == 3:
            clear_screen(t)
            t.penup()
            t.goto(-200, 100)
            t.pendown()
            draw_koch_snowflake(t, 400, 4)
        elif choice == 4:
            clear_screen(t)
            t.penup()
            t.goto(-200, -150)
            t.pendown()
            draw_sierpinski_triangle(t, 400, 4)
        elif choice == 5:
            clear_screen(t)
        elif choice == 6:
            break
        else:
            print("Niepoprawny wybór. Spróbuj ponownie.")

    screen.bye()


if __name__ == "__main__":
    main()
