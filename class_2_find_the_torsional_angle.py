# https://www.hackerrank.com/challenges/class-2-find-the-torsional-angle/problem

import math


class Points(object):
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __sub__(self, no):
        return Points(no.x - self.x, no.y - self.y, no.z - self.z)

    def __repr__(self):
        return f"({self.x}, {self.y}, {self.z})"

    def dot(self, no):
        return no.x * self.x + no.y * self.y + no.z * self.z

    def cross(self, no):
        return Points(
            self.y * no.z - self.z * no.y,
            -(self.x * no.z - self.z * no.x),
            self.x * no.y - self.y * no.x,
        )

    def absolute(self):
        return pow((self.x ** 2 + self.y ** 2 + self.z ** 2), 0.5)
