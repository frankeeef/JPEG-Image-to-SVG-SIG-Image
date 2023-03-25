import cv2
import sys
import numpy as np
import svgwrite

def jpeg_to_svg(jpeg_path, svg_path):
    # Load JPEG image using OpenCV
    img = cv2.imread(jpeg_path)

    # Convert image to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Invert image
    inv_gray = cv2.bitwise_not(gray)

    # Threshold image to make it black and white
    _, thresh = cv2.threshold(inv_gray, 128, 255, cv2.THRESH_BINARY)

    # Find contours in image
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Create SIG/SVG drawing
    drawing = svgwrite.Drawing(filename=svg_path, size=('100%', '100%'))

    # Draw contours on SIG/SVG drawing
    for contour in contours:
        path_data = 'M'
        for point in contour:
            x, y = point[0]
            path_data += f'{x},{y} '
        path_data += 'Z'
        drawing.add(drawing.path(d=path_data, fill='black'))

    # Save SIG/SVG file
    drawing.save()

if __name__ == '__main__':
    jpeg_path = sys.argv[1]
    sig_path = sys.argv[2] + '.' + sys.argv[3]
    jpeg_to_svg(jpeg_path, sig_path)