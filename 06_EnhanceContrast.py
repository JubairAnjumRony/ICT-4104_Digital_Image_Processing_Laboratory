import cv2
# Step 1: Read image
img = cv2.imread('lena.jpg')
# Step 2: Check image
if img is None:
  print("Image not found!")
  exit()
# Step 3: Increase contrast
# alpha = contrast (>1 increases contrast)
# beta = brightness (0 means no brightnesschange)
contrast = cv2.convertScaleAbs(img, alpha=1.8,beta=0)
# Step 4: Show images
cv2.imshow("Original", img)
cv2.imshow("Contrast Enhanced", contrast)
cv2.waitKey(0)
cv2.destroyAllWindows()