import cv2 as cv 

img = cv.imread("Resources/Photos/cat_large2.jpg")

cv.imshow('Cat', img)


# Reading a video 

capture = cv.VideoCapture('Resources/Videos/dog.mp4')

# WE read the video frame by frame 
# while True: 
#     isTrue, frame = capture.read() 
#     cv.imshow('Video', frame)
#     if cv.waitKey(20) & 0xFF == ord('d'): 
#         break
# capture.release() 
# cv.destroyAllWindows()


cv.waitKey(0)