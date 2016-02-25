from argparse import ArgumentParser

from graphics import display, save_extension, Screen
from graphics.draw import draw_line
from graphics.color import RGB_RED, RGB_BLUE, RGB_GREEN, RGB_MAX_VALUE

if __name__ == '__main__':
    parser = ArgumentParser(
        description='Generate images with lines!')
    parser.add_argument('filename', nargs='?', type=str, default='pic.ppm',
        help='the name of the file to be written')
    parser.add_argument('--no-display', action='store_true',
        help='do not attempt to display the image after generating it')
    args = parser.parse_args()
    
    # Start drawing!
    screen = Screen()
    color = RGB_GREEN
    
    xres = screen.get_height()
    yres = screen.get_width()
    
    # Octant I
    draw_line(screen, 0, 0, xres - 1, yres - 75, color)
    # Octant II
    draw_line(screen, 0, 0, xres - 75, yres - 1, color)
    # Octant VIII
    draw_line(screen, 0, yres - 1, xres - 1, 75, color)
    # Octant VII
    draw_line(screen, 0, yres - 1, xres - 75, 0, color)
    
    color = RGB_BLUE
    # Octant V
    draw_line(screen, xres - 1, yres - 1, 0, 75, color)
    # Octant VI
    draw_line(screen, xres - 1, yres - 1, 75, 0, color)
    # Octant IV
    draw_line(screen, xres - 1, 0, 0, yres - 75, color)
    # Octant III
    draw_line(screen, xres - 1, 0, 75, yres - 1, color)
    
    color = RGB_RED
    # y = x
    draw_line(screen, 0, 0, xres - 1, yres - 1, color)
    # y = -x
    draw_line(screen, 0, yres - 1, xres - 1, 0, color)
    
    # horizontal
    draw_line(screen, 0, yres / 2, xres - 1, yres / 2, color)
    # vertical
    draw_line(screen, xres / 2, 0, xres / 2, yres - 1, color)
    
    # display the image
    if not args.no_display:
        display(screen, args.filename)
    else:
        save_extension(screen, args.filename)
