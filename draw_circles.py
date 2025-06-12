import sys
import turtle

def draw_circles(count, radius=50, spacing=20):
    """Draw `count` circles using turtle graphics."""
    t = turtle.Turtle()
    for _ in range(count):
        t.circle(radius)
        t.penup()
        t.forward(2 * radius + spacing)
        t.pendown()
    turtle.done()


def main():
    if len(sys.argv) > 1:
        try:
            count = int(sys.argv[1])
        except ValueError:
            print("Please provide an integer number of circles.")
            return
    else:
        try:
            count = int(input("Enter number of circles: "))
        except ValueError:
            print("Invalid input. Please enter an integer.")
            return
    draw_circles(count)


if __name__ == "__main__":
    main()
