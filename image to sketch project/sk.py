# To convert the image into a sketch do below followed steps

# 1. Convert image into greyscale
# 2. Invert grayscale image
# 3. blur that inverted image
# 4. Mix all above three images into one using inverting blur  
# 5. Now convert that 4 step image into sketch using divide() method.
from operator import invert
import cv2
image = cv2.imread('dog.png')

grey_filter = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
cv2.imwrite("blur.png",grey_filter)

inverted = cv2.bitwise_not(grey_filter)
cv2.imwrite("invert.png",inverted)

blur = cv2.GaussianBlur(inverted,(21,21), 0)
cv2.imwrite("blur.png",inverted)

inverted_blur = cv2.bitwise_not(blur)
cv2.imwrite("inverted_blur.png",inverted)

sketch_filter = cv2.divide(grey_filter,inverted_blur,scale=256.0)

cv2.imwrite("output1.png",sketch_filter)
cv2.imshow("image",image)
cv2.imshow("Sketch",sketch_filter)
cv2.waitKey(0)


