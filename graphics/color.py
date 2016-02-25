# Standard color positions in lists and tuples
RED = 0
GREEN = 1
BLUE = 2

# Shortcut rgb values
RGB_MAX_VALUE = 255
RGB_BLACK = (0, 0, 0)
RGB_BLUE = (0, 0, 255)
RGB_GREEN = (0, 255, 0)
RGB_RED = (255, 0, 0)
RGB_WHITE = (255, 255, 255)

class Color(object):
    def __init__(self, color=RGB_BLACK):
        if isinstance(color, str):
            color = hex_to_rgb(color)
        elif isinstance(color, Color):
            color = (color.r, color.g, color.b)
        self.r = self.red = int(color[RED])
        self.g = self.green = int(color[GREEN])
        self.b = self.blue = int(color[BLUE])
    
    def __iter__(self):
        for v in self.to_rgb():
            yield v
    
    def __repr__(self):
        return 'Color({}, {}, {})'.format(*self.to_rgb())
    
    def __str__(self):
        return unicode(self).encode('utf-8')
    
    def __unicode__(self):
        return self.to_hex()
    
    def to_hex(self):
        return rgb_to_hex(self.to_rgb())
    
    def to_rgb(self):
        return (self.r, self.g, self.b)

def hex_to_rgb(color):
    if len(color) == 7 or len(color) == 4:
        color = color[1:]
    c = tuple(int( # Just assume the function is being used properly for now.
                (color[i*2:i*2+2] if len(color) == 6 else color[i:i+1] * 2),
                16
            ) for i in range(3))
    return c

def rgb_to_hex(color):
    return '#{:02x}{:02x}{:02x}'.format(color[RED], color[GREEN], color[BLUE])