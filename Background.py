import cv2 #opencv for image processing
# creating a videocapture cobjectca
cap = cv2.VideoCapture(0)  # this is my webcam
# get the background image
while cap.isOpened():
    ret, background = cap.read() #simply reading from background
    if ret:
        cv2.imshow("image", background)
        if cv2.waitKey(4)== ord('q'):
            #save the background image
            cv2.imwrite("image.jpg", background)
            break
cap.release()
cv2.destroyAllWindows()