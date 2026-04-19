import cv2
img = cv2.imread('lena.jpg')
if img is None:
    print("Image not found!")
    exit()
    
#if grayscale image
if len(img.shape) == 2:
    enhanced = cv2.equalizeHist(img)
    cv2.imshow("Original",img)
    cv2.imshow("Enhanced",enhanced)
 
else:
    #RGB Image enhancement (simple brightness+contrast Boost)
    enhanced = cv2.convertScaleAbs(img,alpha=1.3,beta=30)
    
    cv2.imshow("Original",img)
    cv2.imshow("Enhanced",enhanced) 


cv2.waitKey(0)
cv2.destroyAllWindows()       