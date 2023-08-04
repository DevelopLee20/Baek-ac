textline = [iter(input()) for __ in range(5)]

while 1:
    a = next(textline[0], "$")
    b = next(textline[1], "$")
    c = next(textline[2], "$")
    d = next(textline[3], "$")
    e = next(textline[4], "$")

    if a+b+c+d+e == "$$$$$":
        break
    else:
        if a != "$":
            print(a, end="")
        if b != "$":
            print(b, end="")
        if c != "$":
            print(c, end="")
        if d != "$":
            print(d, end="")
        if e != "$":
            print(e, end="")
