import cv2
import numpy as np
#step 1: Read image
img = cv2.imread('lena.jpg')

#step2: Check image
if img is None:
    print("Image not found!")
    exit()

#step 3: Define sharpening kernel
kernel = np.array([[0,-1,0],
                  [-1,5,-1],
                  [0,-1,0]])

#step 4:Apply filter (convolution)
sharpened = cv2.filter2D(img,-1,kernel)

#step 5: show images
cv2.imshow("Original",img)
cv2.imshow("Sharpened Image",sharpened)

cv2.waitKey(0)
cv2.destroyAllWindows()