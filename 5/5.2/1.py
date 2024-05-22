from math import sqrt


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self, x, y):
        self.x += x
        self.y += y

    def length(self, point):
        return round(sqrt(abs(self.x - point.x)**2 + abs(self.y - point.y)**2), 2)


class PatchedPoint(Point):
    def __init__(self, *args):
        if len(args) == 0:
            self.x = 0
            self.y = 0
        elif len(args) == 1:
            self.x, self.y = args[0]
        elif len(args) > 1:
            self.x = args[0]
            self.y = args[1]


first_point = PatchedPoint((2, -7))
second_point = PatchedPoint(7, 9)
print(first_point.length(second_point))
print(second_point.length(first_point))
