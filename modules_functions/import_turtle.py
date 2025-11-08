import turtle
from math import radians, cos


def square (length: int) -> None:
    """Draw Square"""
    for s in range(4):
        turtle.forward(length)
        turtle.right(90)

# for i in range(72):  
#     square(120)
#     turtle.left(5)
# turtle.done()

def encircled_square(length: int) -> None:
    square(length)
    angle = radians(45)
    radius = length * cos(angle)
    turtle.right(135)
    turtle.circle(radius)
    print(f'Inside function, namespace is: {dir()}')
    print(f'locals: {locals()}')
    
encircled_square(300)

print(globals())

# turtle.speed('fast')
# for i in range(72):
#     encircled_square(120)
#     turtle.left(5)
# turtle.done()