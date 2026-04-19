import cv2
#step 1: Read Image
img = cv2.imread('lena.jpg')

#step 2: Check image
if img is None:
    print("Error: Image not found")
    exit()


#step 3:Apply Gaussian Filter
#(5,5) = kernel size, 0 = auto sigma
blurred = cv2.GaussianBlur(img,(5,5),0)

#step 4: show images
cv2.imshow("Original Image",img)
cv2.imshow("Gaussian Smoothed Image",blurred)

cv2.waitKey(0)
cv2.destroyAllWindows()