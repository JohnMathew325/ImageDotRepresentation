# Converts an image into braille characters
# Requires a unicode supporting output method
# Works best on cartoon-like images with few edges

import braille_chars as bc
from PIL import Image
from sys import argv


def nearest_multiple(n, m):
    """
    Returns the multiple of m closest to n
    """

    return round(n / m) * m

# parse command line arguments
if len(argv) < 2:
    print("Error: no path specefied")
    exit(1)
else:
    path = argv[1]

scale = 1 if len(argv) < 3 else float(argv[2])

# load and scale image
img = Image.open(path).convert("RGB")
width = nearest_multiple(img.size[0] * scale, bc.WIDTH)
height = nearest_multiple(img.size[1] * scale, bc.HEIGHT)
img = img.resize((width, height), Image.NEAREST)

#get the image as grayscale values
pixel_values = []

for y in range(height):
    for x in range(width):
        pixel_values.append(sum(img.getpixel((x, y))) // 3)

# print the image as braile characters
for y in range(0, height, bc.HEIGHT):
    for x in range(0, width, bc.WIDTH):
        valvec = []

        for o in range(bc.HEIGHT):
            i = x + (y + o) * width
            valvec += pixel_values[i:i + 2]

        average_value = sum(valvec) // len(valvec)
        print(bc.from_bitvec([v < average_value for v in valvec]), end="", flush=False)

    print(flush=False)
