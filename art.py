import random, os, sys

def get_rgb():
    """
    makes a semi-random rgb
    """
    colors = [0, 0, 0]
    colors[0] = random.randint(1, 255)
    if colors[0] == 255:
        colors[1] = random.randint(0, 100)
    else:
        colors[1] = random.randint(0, 255)
    if colors[1] == 255 or colors[0] == 255:
        colors[2] = random.randint(0, 100)
    else:
        colors[2] = random.randint(0, 255)

    if colors[0] != 255 or colors[1] != 255 or colors[2] != 255:
        colors[random.randint(0, 2)] = 255

    rgb = "\"rgb(" + str(colors[0]) + "," + str(colors[1]) + "," + str(colors[2]) + ")\""
    return rgb

def random_circle():
    """
    generates a random circle in a random position on the map
    """
    x = random.randint(0, 1280) # center coordinates
    y = random.randint(0, 1280) # center coordinates
    x2 = x + random.randint(0, 50) #edge coordinates
    y2 = y + random.randint(0, 50) #edge coordinates

    item = "circle " + str(x) + "," + str(y) + " " + str(x2) + "," + str(y2)

    return item

def stroke(strokewidth, stroke_color, coord, dim, angle):
    """
     "" ellipse ""
    """
    x = coord[0]
    y = coord[1]
    width = dim[0]
    height = dim[1]
    start_angle = angle[0]
    finish_angle = angle[1]
    line = " fill none stroke-linecap round stroke-width " + str(strokewidth) + " stroke "
    line += str(stroke_color) + " ellipse " + str(x) + "," + str(y) + " "
    line += str(width) + "," + str(height) + " "
    line += str(start_angle) + "," + str(finish_angle)

    return line

def random_stroke():
    """
     "" random ellipse ""
    """
    strokewidth = random.randint(5, 200)
    stroke_color = get_rgb()
    x = random.randint(20, 1280)
    y = random.randint(20, 1280)
    width = random.randint(20, 350)
    height = random.randint(20, 350)
    start_angle = random.randint(0, 360)
    finish_angle = random.randint(0, 360)

    line = " fill none stroke-linecap round stroke-width " + str(strokewidth) + " stroke "
    line += str(stroke_color) + " ellipse " + str(x) + "," + str(y) + " "
    line += str(width) + "," + str(height) + " "
    line += str(start_angle) + "," + str(finish_angle)

    return line

"""
"""
"""
"""

def command(number):
    """
    generates command
    """
    name = "art"
    thing = "convert -size 1280x1280 xc: -draw \'"
    for i in range(number):
        thing += "fill " + get_rgb() + " " + random_stroke() + " "
    thing += "\' " + name + ".jpeg "
    return thing

if __name__ == "__main__":
    print("generating . . . ")
    word = command(int(sys.argv[1]))
    print("executing . . . ")
    os.system(word)
