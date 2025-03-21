from point import Point
import random

class Colorpoint:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color

    def __str__(self):
        return f"[{self.color}: {self.x}, {self.y}]"

p = Colorpoint(1, 1, "red")
print(p)

colors = ["red", 'green', 'yellow', 'black', 'magenta', 'cyan', 'white', 'marsala']

color_points = []

for i in range(10):
    color_points.append(Colorpoint(random.randint(-10, 10), random.randint(-10, 10), random.choice(colors)))

print(color_points)
color_points.sort()

print(color_points)