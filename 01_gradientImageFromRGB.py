import cv2
import numpy as np

# Step 1: Read image
img = cv2.imread('lena.jpg')

# Step 2: Check image
if img is None:
  print("Error: Image not found!")
  exit()

# Step 3: Convert to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Step 4: Apply Sobel in X direction
grad_x = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=3)

# Step 5: Apply Sobel in Y direction
grad_y = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=3)

# Step 6: Gradient magnitude
gradient = cv2.magnitude(grad_x, grad_y)

# Step 7: Convert to displayable format
grad_x = cv2.convertScaleAbs(grad_x)
grad_y = cv2.convertScaleAbs(grad_y)
gradient = cv2.convertScaleAbs(gradient)

# Step 8: Show output
cv2.imshow("Original Image", img)
cv2.imshow("Grayscale", gray)
cv2.imshow("Gradient X", grad_x)
cv2.imshow("Gradient Y", grad_y)
cv2.imshow("Final Gradient", gradient)

cv2.waitKey(0)
cv2.destroyAllWindows()