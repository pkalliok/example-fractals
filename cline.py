from turtle import fd, rt, lt, bk

def cline(minl, length):
    if length < minl:
        fd(length)
        return
    lt(90)
    cline(minl, length/2.)
    rt(90)
    cline(minl, length/2.)
    cline(minl, length/2.)
    rt(90)
    cline(minl, length/2.)
    lt(90)

def sierp(minl, length):
    for i in range(3):
        if length > minl:
            sierp(minl, length/2.)
        fd(length)
        rt(120)

