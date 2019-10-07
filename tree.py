from turtle import fd, rt, lt, bk

def tree(minl, length):
    if length < minl:
        fd(length)
        bk(length)
        return
    fd(length)
    lt(25)
    tree(minl, length * .8)
    rt(75)
    tree(minl, length * .5)
    lt(50)
    bk(length)
