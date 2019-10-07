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

