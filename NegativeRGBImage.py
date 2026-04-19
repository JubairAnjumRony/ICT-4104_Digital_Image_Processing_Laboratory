import cv2

# Read color image
img = cv2.imread('m.jpg')

# Check image
if img is None:
 print("Error: Image not found!")
else:
 # Convert to negative
 negative = 255 - img

 # Show images
 cv2.imshow("Original Image", img)
 cv2.imshow("Negative Image", negative)

 cv2.waitKey(0)
 cv2.destroyAllWindows()