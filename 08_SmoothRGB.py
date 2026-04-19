import cv2
#step 1: Read Image
img = cv2.imread('lena.jpg')

#step 2: Check image
if img is None:
    print("Error: Image not found!")
    exit()


#step 3: Apply Average Filter (Blur)
#(5,5) means 5*5 Kernel
blurred = cv2.blur(img,(5,5))

#step 4: Show images
cv2.imshow("Original Image",img)
cv2.imshow("Smoothed Image(Average Filter)",blurred)

#step5: wait and close
cv2.waitKey(0)
cv2.destroyAllWindows()