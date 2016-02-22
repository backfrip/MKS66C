
class Color(object):
    DEFAULT_RED = 0
    DEFAULT_GREEN = 0
    DEFAULT_BLUE = 0
    
    def __init__(self, red=DEFAULT_RED, green=DEFAULT_GREEN, blue=DEFAULT_BLUE):
        self.red = red
        self.green = green
        self.blue = blue
    
    def __repr__(self):
        return 'Color({}, {}, {})'.format(self.red, self.green, self.blue)
    
    def __str__(self):
        return unicode(self).encode('utf-8')
    
    def __unicode__(self):
        return '#{:02x}{:02x}{:02x}'.format(self.red, self.green, self.blue)

class Screen(object):
    DEFAULT_WIDTH = 500
    DEFAULT_HEIGHT = 500
    
    def __init__(self, width=DEFAULT_WIDTH, height=DEFAULT_HEIGHT):
        self.width = width
        self.height = height
