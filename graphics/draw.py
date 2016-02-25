
def draw_line(screen, x0, y0, x1, y1, color):
    if x0 == x1: # vertical
        for dy in range(abs(y1 - y0)):
            screen.plot(x0, y0 + dy, color)
        return
    if y0 == y1: # horizontal
        for dx in range(abs(x1 - x0)):
            screen.plot(x0 + dx, y0, color)
        return
    if x0 > x1: # drawing right to left, flip coordinates
        x0, x1 = (x1, x0)
        y0, y1 = (y1, y0)
    A = y1 - y0
    B = -(x1 - x0)
    m = float(A) / -B
    
    a = [x0]
    da = 1
    db = 1
    if m > 1: # II and VI
        d = [0, A + 2*B]
        a = [y0]
        b = [x0]
        c = [b, a]
        f = y1
        d0 = -2*A
        d1 = -2*B
    elif m > 0: # I and V
        d = [2*A + B, 0]
        b = [y0]
        c = [a, b]
        f = x1
        d0 = 2*B
        d1 = 2*A
    elif m > -1: # IV and VIII
        d = [0, 2*A - B]
        b = [y0]
        c = [a, b]
        f = x1
        db = -1
        d0 = 2*B
        d1 = -2*A
    else: # III and VII
        d = [A - 2*B, 0]
        a = [y1]
        b = [x1]
        c = [b, a]
        f = y0
        db = -1
        d0 = 2*A
        d1 = -2*B
    
    while a[0] <= f:
        screen.plot(c[0][0], c[1][0], color)
        if d[0] > d[1]:
            b[0] += db
            d[0] += d0
        a[0] += da
        d[0] += d1
