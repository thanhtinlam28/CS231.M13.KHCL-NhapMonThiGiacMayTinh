#import packages
import imutils
import cv2

#Load the input image and show its dimensions
image = cv2.imread("rab.jpg")
(h, w, d) = image.shape
print("width={}, height={}, depth={}".format(w,h,d))

#Display image
cv2.imshow("Image", image)
cv2.waitKey(0)

#access the RGB pixel located at x=50, y=100.
#OpenCV stores images in BGR
(B, G, R) = image[100,50]
print("R={}, G={}, B={}".format(R, G, B))

# extract a 100x100 pixel square ROI (Region of Interest) from the
# input image starting at x=230,y=60 at ending at x=430,y=230
roi = image[60:230, 230:430]
cv2.imshow("ROI", roi)
cv2.waitKey(0)

# resize the image to 200x200px, ignoring aspect ratio
resized = cv2.resize(image, (200, 200))
cv2.imshow("Fixed Resizing", resized)
cv2.waitKey(0)

# fixed resizing and distort aspect ratio so let's resize the width
# to be 300px but compute the new height based on the aspect ratio
r = 300.0 / w
dim = (300, int(h * r))
resized = cv2.resize(image, dim)
cv2.imshow("Aspect Ratio Resize", resized)
cv2.waitKey(0)