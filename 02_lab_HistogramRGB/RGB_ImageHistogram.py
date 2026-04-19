import cv2
import matplotlib.pyplot as plt

# Read color image
img = cv2.imread('m.jpg')

# Check image
if img is None:
  print("Error: Image not found!")
else: # Show image 
   cv2.imshow("Color Image", img)
 # Colors for each channel
   colors = ('b', 'g', 'r')
   for i, col in enumerate(colors):
     hist = cv2.calcHist([img], [i], None, [256], [0, 256])
     plt.plot(hist, color=col)
   plt.title("RGB Histogram") 
   plt.xlabel("Pixel Value")
   plt.ylabel("Frequency")
   plt.show()
   cv2.waitKey(0) 
   cv2.destroyAllWindows()