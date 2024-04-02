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

