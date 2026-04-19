import cv2

#step 1: Read Image
img = cv2.imread('lena.jpg',0)

#step 2: Check image
if img is None:
    print("Image not found!")
    exit()

#step 3: Increase Brightness
#alpha = contrast(1.0 = same)
#beta = brightness value(increase this to make image brighter)
bright = cv2.convertScaleAbs(img, alpha=1.0,beta=50)

#step4: show images
cv2.imshow("Original",img)
cv2.imshow("Bright Image",bright)

cv2.waitKey(0)
cv2.destroyAllWindows()