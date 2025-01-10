from PIL import Image
import colorsys
import math
import time
from concurrent.futures import ThreadPoolExecutor


def logColor(distance, base, const, scale):
    color = -1 * math.log(distance, base)
    rgb = colorsys.hsv_to_rgb(const + scale * color, 0.8, 0.9)
    return tuple(round(i * 255) for i in rgb)


def generate_row(row, width, height, minX, maxY, xRange, yRange, precision):
    pixels_row = [None] * width
    for col in range(width):
        c = 0
        c0 = complex(minX + col * xRange / width, maxY - row * yRange / height)

        for i in range(precision + 1):
            if abs(c) > 2:
                break
            c = c * c + c0

        if i < precision:
            distance = (i + 1) / (precision + 1)
            rgb = logColor(distance, 0.2, 0.27, 1.0)
            pixels_row[col] = rgb
        else:
            pixels_row[col] = (0, 0, 0)
    return row, pixels_row


def main():
    # Image frame parameters
    width = 3840  # pixels
    aspectRatio = 16 / 9
    height = round(width / aspectRatio)

    # Number of precision count checks
    precision = 500

    x = -0.65
    y = 0
    xRange = 3.4

    yRange = xRange / aspectRatio
    minX = x - xRange / 2
    maxY = y + yRange / 2

    image = Image.new('RGB', (width, height), color='black')
    pixels = image.load()

    # Start time
    startTime = time.time()

    # Loop for generating the image
    with ThreadPoolExecutor() as executor:
        futures = [
            executor.submit(generate_row, row, width, height, minX, maxY, xRange, yRange, precision)
            for row in range(height)
        ]

        for future in futures:
            row, row_pixels = future.result()
            for col, color in enumerate(row_pixels):
                pixels[col, row] = color

    # Calculate execution time
    endTime = time.time()
    print("Execution time: ", endTime - startTime)
    image.show()
    image.save('output.png')


if __name__ == "__main__":
    main()