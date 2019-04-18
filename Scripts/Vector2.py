from math import *


class Vector2:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def __add__(self,vector):
        if (self.x and self.y) is type(int) or (self.x and self.y) is type(float):
            return Vector2(self.x + vector.x, self.y + vector.y)
        else:
            raise TypeError("x and y must be of type int or float")

    def __sub__(self, other):
        return Vector2(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        if type(other) is Vector2:
            return Vector2(self.x * other.x, self.y * other.y)
        elif type(other) is int or type(other) is float:
            return Vector2(self.x * other, self.y * other)
        # else:
        #    raise TypeError("unsupported operand type for " + str(type(Vector2)) + " and " + str(type(other)))

    def Magnitude(self):
        return sqrt(self.x ** 2 + self.y ** 2)

    def sqrtMagnitude(self):
        return self.x ** 2 + self.y ** 2


zero = Vector2(0,0)
one = Vector2(1,1)
right = Vector2(1,0)
up = Vector2(0,1)
left = Vector2(-1,0)
down = Vector2(0,-1)

