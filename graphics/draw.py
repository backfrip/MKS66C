
def draw_line(screen, x0, y0, x1, y1, color):
    """This is technically the Bresenham line algorithm, even
    if there's no way a human could possibly read it. I kinda
    spent some time squishing it down.
    """
    
    if x0 == x1: # Vertical
        for dy in range(abs(y1 - y0)):
            screen.plot(x0, y0 + dy, color)
        return
    if y0 == y1: # Horizontal
        for dx in range(abs(x1 - x0)):
            screen.plot(x0 + dx, y0, color)
        return
    
    if x0 > x1: # Drawing right to left, flip coordinates
        x0, x1 = (x1, x0)
        y0, y1 = (y1, y0)
    
    A = y1 - y0
    B = -(x1 - x0)
    m = float(A) / -B
    
    if -1 <= m < 1:
        d, db, d1 = (
            # Octants I and V
            [2*A+B, 0], 1, 2*A
        ) if 0 <= m else (
            # Octants IV and VIII
            [0, 2*A-B], -1, -2*A
        )
        a, b = [x0], [y0]
        c, f, d0 = [a, b], x1, 2*B
    else:
        d, a, b, f, db, d0 = (
            # Octants II and VI
            [0, A+2*B], [y0], [x0], y1, 1, -2*A
        ) if 1 <= m else (
            # Octants III and VII
            [A-2*B, 0], [y1], [x1], y0, -1, 2*A
        )
        c, d1 = [b, a], -2*B
    
    # Draw the actual line
    while a[0] <= f:
        screen.plot(c[0][0], c[1][0], color)
        if d[0] > d[1]:
            b[0] += db
            d[0] += d0
        a[0] += 1
        d[0] += d1
