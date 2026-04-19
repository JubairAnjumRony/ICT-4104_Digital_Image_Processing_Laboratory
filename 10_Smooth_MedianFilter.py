import cv2

#step 1: Read image
img = cv2.imread('lena.jpg')

#step 2: Check Image
if img is None:
    print("Error: Image not found!")
    exit()

#step 3: Apply Median Filter
#5 = kernel size (Must be odd)

blurred = cv2.medianBlur(img,5)

#step 4: show images
cv2.imshow("original Image",img)
cv2.imshow("Median Smoothed Image",blurred)

cv2.waitKey(0)
cv2.destroyAllWindows()