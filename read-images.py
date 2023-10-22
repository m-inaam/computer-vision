import cv2 as cv 

# Read image
img = cv.imread("Resources/Photos/cat.jpg")

# Resize image
# imgResize = cv.resize(img, (1000, 500))

# Get the shape of the resized image
# print(imgResize.shape)  # This line will display the shape of the image

# Crop image
# imgCropped = img[0:200, 200:500] # [height, width]

cv.imshow("Image", img)
# cv.imshow("Image Resize", imgResize)
# cv.imshow("Image Cropped", imgCropped)

cv.waitKey(0)
cv.destroyAllWindows()