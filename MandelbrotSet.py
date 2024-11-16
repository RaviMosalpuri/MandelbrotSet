from PIL import Image
import colorsys
import math
import os

def logColor(distance, base, const, scale):
    color = -1 * math.log(distance, base)
    rgb = colorsys.hsv_to_rgb(const + scale * color,0.8,0.9)
    return tuple(round(i * 255) for i in rgb)


def powerColor(distance, exp, const, scale):
    color = distance**exp
    rgb = colorsys.hsv_to_rgb(const + scale * color,1 - 0.6 * color,0.9)
    return tuple(round(i * 255) for i in rgb)


def main():
    # Image frame parameters
    width = 1000 # pixels
    aspectRatio = 4/3
    height = round(width / aspectRatio)

    precision = 500

    x = -0.65
    y = 0
    xRange = 3.4

    yRange = xRange / aspectRatio
    minX = x - xRange / 2
    maxY = y + yRange / 2

    image = Image.new('RGB', (width, height), color = 'black')
    pixels = image.load()

    for row in range(height):
        for col in range(width):
            x = minX + col * xRange / width
            y = maxY - row * yRange / height
            oldX = x
            oldY = y

            for i in range(precision + 1):
                a = x*x - y*y # real component of z^2
                b = 2 * x * y # imaginary component of z^2
                x = a + oldX # real component of new z
                y = b + oldY # imaginary component of new z
                if x*x + y*y > 4:
                    break
            
            if i < precision:
                distance = (i + 1) / (precision + 1)
                rgb = logColor(distance, 0.2, 0.27, 1.0)
                pixels[col,row] = rgb
            
            index = row * width + col + 1
            print("{} / {}, {}%".format(index, width * height, round(index / width / height * 100 * 10) / 10))

    image.save('output.png')

    return


if __name__ == "__main__":
    main()