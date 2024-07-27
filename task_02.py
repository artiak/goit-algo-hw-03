"""
Provides solution for Coch Curve drawing.
"""
from turtle import Screen
from turtle import Turtle


def draw_koch_snowflake(order: int, size: int = 300):
    """
    Draws Koch Curve using recursive approach.
    """
    turtle: Turtle = _create_turtle(size)

    _koch_curve(turtle, order, size)

    for _ in range(1, 3):
        turtle.left(-120)
        _koch_curve(turtle, order, size)

    screen: Screen = _create_screen()
    screen.mainloop()


def _create_turtle(size):
    turtle = Turtle()
    turtle.speed(1)
    turtle.penup()
    turtle.goto(-size / 2, 0)
    turtle.pendown()

    return turtle


def _koch_curve(turtle: Turtle, order: int, size: int) -> None:
    if order == 0:
        turtle.forward(size)

        return

    for angle in [60, -120, 60, 0]:
        _koch_curve(turtle, order - 1, size / 3)
        turtle.left(angle)


def _create_screen():
    screen = Screen()
    screen.bgcolor("white")

    return screen


if __name__ == "__main__":
    draw_koch_snowflake(1)
