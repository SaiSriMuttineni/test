def sortedthree(a, b, c):
    if (a > b):
        if (b > c) :
            return (c, b, a)
        else:
            return (b, c, a)
    else:
    if (a > c):
            return (c, a, b)
        else:
            return (a, b, c)
assert (sortedthree(1, 2, 3) == (1, 2, 3))
assert (sortedthree(3, 2, 1) == (1, 2, 3))
