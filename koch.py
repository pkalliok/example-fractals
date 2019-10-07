from turtle import fd, rt, lt, bk

def koch(minl, length):
    if length < minl:
        fd(length)
        return
    koch(minl, length/3.)
    lt(60)
    koch(minl, length/3.)
    rt(120)
    koch(minl, length/3.)
    lt(60)
    koch(minl, length/3.)

def fan(minl, length):
    if length < minl:
        fd(length)
        return
    fan(minl, length/2.)
    lt(60)
    fd(length/2.)
    rt(120)
    fan(minl, length/2.)
    lt(60)

