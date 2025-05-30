from math import sqrt

"""
ارین مفتوح
حل تمرین دو و سه
"""


class Triangle:

    def __init__(self, lvl=0):
        self.lvl = lvl
        self.symbol = "* "

    def get_rig(self):
        return self.lvl // 2 * (self.lvl + 1)

    def changeSymbol(self, char):
        self.symbol = char + " "

    def get_lvl(self):
        return self.lvl

    def solveTriangle(self, m):
        delta = 1 + 8 * m
        if delta < 0:
            return 0
        n = (-1 + sqrt(delta)) / 2
        return n

    def isTriangle(self, rig):
        return int(self.solveTriangle(rig) % 1 == 0)

    def getTrangleFromRig(self, rig):
        if self.isTriangle(rig):
            self.lvl = int(self.solveTriangle(rig))

    def __add__(self, other):
        if isinstance(other, Triangle):
            return Triangle(other.lvl + self.lvl)
        elif isinstance(other, int):
            return Triangle(self.lvl + other)

    def __str__(self):
        full_tree = ""
        space = self.lvl - 1
        for i in range(self.lvl):
            full_tree = full_tree + space * " " + i * self.symbol + "\n"
            space -= 1
        return full_tree


def triangle(n):
    space = n - 1
    for i in range(n):
        if i == 0 or i == n - 1:
            print(space * " " + (2 * i + 1) * "*")
        else:
            print(space * " " + "*" + (2 * i - 1) * "O" + "*")
        space -= 1


def triangle2(n):
    for i in range(n):
        print(((n - i) // 2) * " "+ "*"+ ((2 * i + 1) - 2) * "O"+ int(((2 * i + 1) - 2) > 0) * "*")


if __name__ == "__main__":
    triangle(7)
    triangle(5)
    triangle2(2)
    triangle(11)
