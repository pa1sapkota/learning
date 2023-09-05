# basic function in the opencv 

import cv2 as cv 
img = cv.imread('Resources/Photos/park.jpg')
cv.imshow("Cat", img)

#Converting to the grayscale image 

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)



# Blurring an Image 
blur = cv.GaussianBlur(img , (7,7),cv.BORDER_DEFAULT ) # the second parameter should be of the odd 

cv.imshow("Blurry", blur)

# Edge Cascade 

canny = cv.Canny(img, 125, 175)
cv.imshow('Canny Image', canny)


# we can use the blurr to get the egdes clearly 
canny2 = cv.Canny(blur, 125,175 )
cv.imshow("Canny 2", canny2)

# Dilate the image 
dilated = cv.dilate(canny, (7,7), iterations=3)
cv.imshow("Dilated",dilated)


# Resize and Crop Image 
resized = cv.resize(img, (500,500), interpolation= cv.INTER_CUBIC)
cv.imshow("Resized", resized)

# Cropped image 
cropped = img[50:200, 200:400]
cv.imshow(cropped)


cv.waitKey(0)
