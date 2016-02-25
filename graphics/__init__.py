import color
import os
from sys import stdin, stdout
from subprocess import call

class Screen(object):
    DEFAULT_WIDTH = 500
    DEFAULT_HEIGHT = 500
    
    def __init__(self, width=DEFAULT_WIDTH,
            height=DEFAULT_HEIGHT, base_color=color.RGB_BLACK):
        self._width = width
        self._height = height
        self._color = base_color
        self.clear()
    
    def __getitem__(self, key):
        if type(key) is int or type(key) is slice:
            return self._screen[key]
        raise TypeError('invalid key: ' + repr(key))
    
    def __repr__(self):
        return 'Screen({}, {}, \'{}\')'.format(
            self._width, self._height, color.rgb_to_hex(self._color))
    
    def __str__(self):
        return unicode(self).encode('utf-8')
    
    def __unicode__(self):
        return '\n'.join(
            ' '.join(str(c) for c in row) for row in self)
    
    def clear(self):
        self._screen = [
            [color.Color(self._color) for
                _ in range(self._width)] for
                    _ in range(self._height)]
    
    def get_base_color(self):
        return Color(self._color)
    
    def get_height(self):
        return self._height
    
    def get_width(self):
        return self._width
    
    def plot(self, x, y, color_):
        self[self._height - 1 - y][x] = color.Color(color_)
    
    def save_as_ppm(self, file):
        out = 'P3\n{width} {height} 255\n{rows}\n'.format(
            width=self._width, height=self._height,
            rows = '\n'.join(
                ' '.join(
                    ' '.join(str(v) for v in c) for
                        c in row) for row in self)
        )
        with file:
            file.write(out)
    
    def set_base_color(self, base_color):
        self._color = Color(base_color).to_rgb()

# The below functions exist for [vague] compatability purposes
# and mimic the functionality of `dwsource/display.py`.
def new_screen(width=Screen.DEFAULT_WIDTH, height=Screen.DEFAULT_HEIGHT):
    return Screen(width, height)

def plot(screen, color, x, y):
    screen.plot(x, y, color)

def clear_screen(screen):
    screen.clear()

def save_ppm(screen, fname):
    print 'Generating "{}"...'.format(fname)
    screen.save_as_ppm(open(fname, 'w'))

# The below functions assume that imagemagick is installed.
def save_extension(screen, fname):
    pname, extension = os.path.splitext(fname)
    if extension != '.ppm':
        pname += '.ppm'
        save_ppm(screen, pname)
        print 'Converting "{}" to "{}"...'.format(pname, fname)
        call(['convert', pname, fname], stdin=stdin, stdout=stdout)
        print 'Removing "{}"...'.format(pname)
        os.remove(pname)
    else:
        save_ppm(screen, fname)

def display(screen, fname='pic.ppm'):
    save_extension(screen, fname)
    call(['display', fname], stdin=stdin, stdout=stdout)
