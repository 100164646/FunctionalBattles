# Adam Mazrouea
# 10/02/2023
# Functional Battles
import math


def periRect(l, w):
    return l + l + w + w


def trapArea(b1, b2, h):
    return ((b1 + b2) / 2) * h


def conicVol(r, h):
    return math.pi * math.pow(r,2) * (h / 3)


def cubicBarrier(s):
    return 6 * (math.pow(a,2))


def blastArea(r):
    return math.pi * (math.pow(r,2))


def elevationVect(x1, y1, x2, y2):
    return (y2 - y1) / (x2 - x1)


def atmoShift(f):
    return (f - 32) * 5/9


# add more tests to make sure your functions are correctly working
print(periRect(12, 5))

print("{0:.1f}".format(trapArea(3, 3, 3)))

print("{0:.2f}".format(conicVol(4, 4)))

print("{0:.1f}".format(blastArea(7.5)))

print("{0:.2f}".format(elevationVect(1, 9, 14, 2)))

print("{0:.2f}".format(atmoShift(98.6)) + " degrees celsius")
