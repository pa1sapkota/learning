import cv2 as cv 


img = cv.imread('Resources/Photos/cat.jpg')
cv.imshow('cat', img)

def changeRes(width , height): 
    # Live Video 
    capture.set(3, width)
    capture.set(4, height)


def rescaleFrame(frame , scale = 0.75): 
    # Images , Videos , Live Video 
    width = int(frame.shape[1] * scale )
    height = int(frame.shape[0] * scale )
    dimension = (width, height)
    
    return cv.resize(frame, dimension , interpolation=cv.INTER_AREA)

rescale_frame = rescaleFrame(img)
cv.imshow("Rescaled Cat", rescale_frame)
cv.imshow("Cat", img)
capture = cv.VideoCapture('Resources/Videos/dog.mp4')

# WE read the video frame by frame 
while True: 
    isTrue, frame = capture.read() 
    frame_resized = rescaleFrame(frame , )
    cv.imshow('Video', frame)
    cv.imshow('Video Resized', frame_resized)
    if cv.waitKey(20) & 0xFF == ord('d'): 
        break
capture.release() 
cv.destroyAllWindows()



cv.waitKey(0)