import cv2
import matplotlib.pyplot as plt
     
    # Read image in grayscale
img = cv2.imread('lena.jpg', 0)
     
     # Check image loaded or not
if img is None:
      print("Error: Image not found!")
else:
     # Show image
      cv2.imshow("Grayscale Image", img) 
      # Plot histogram
      plt.hist(img.ravel(), 256, [0, 256])
      plt.title("Grayscale Histogram")
      plt.xlabel("Pixel Value")
      plt.ylabel("Frequency")
      plt.show()
     
      cv2.waitKey(0)
      cv2.destroyAllWindows()