import cv2
import numpy as np

def preprocess_image(image_path):
    # Load and convert to grayscale
    img = cv2.imread(image_path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Apply Gaussian blur
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)

    # Equalize histogram
    equalized = cv2.equalizeHist(blurred)

    # Thresholding
    _, thresh = cv2.threshold(equalized, 127, 255, cv2.THRESH_BINARY)

    # Find contours
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Draw contours
    output = img.copy()
    cv2.drawContours(output, contours, -1, (0, 255, 0), 2)

    return output, contours

def show_result(image_path):
    result, _ = preprocess_image(image_path)
    cv2.imshow("Processed Image", result)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == '__main__':
    import sys
    if len(sys.argv) > 1:
        show_result(sys.argv[1])
    else:
        print("Usage: python filter.py <image_path>")
