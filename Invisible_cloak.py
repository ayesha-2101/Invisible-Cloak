import cv2  #for image processing
import numpy as np #this is a mathematical libary for handling image

cap= cv2.VideoCapture(0)
background = cv2.imread('./image.jpg')

while cap.isOpened():
    #capture the live frame
    ret, current_frame = cap.read()
    if ret:
        #converting from rgb to hsv
        hsv_frame= cv2.cvtColor(current_frame, cv2.COLOR_BGR2HSV)
        
        #set the range for lower red
        l_red = np.array([0,120,70])
        U_red = np.array([10,225,225])
        mask1 = cv2.inRange(hsv_frame,l_red,U_red)
       
       #range for upper red
        l_red = np.array([170,120,70])
        U_red = np.array([180,225,225])
        mask2 = cv2.inRange(hsv_frame,l_red,U_red)

        #generating the final red mask
        red_mask = mask1 + mask2
        red_mask = cv2.morphologyEx(red_mask, cv2.MORPH_OPEN, np.ones((3,3),np.uint8),iterations=10)
        red_mask = cv2.morphologyEx(red_mask, cv2.MORPH_DILATE, np.ones((3,3),np.uint8),iterations=1)
        
        #subsituting the red portin with background image
        part1 = cv2.bitwise_and(background, background, mask= red_mask)
        
        #detecting things that are not red
        red_free = cv2.bitwise_not(red_mask)

        #if cloak is not present show the current image
        part2 = cv2.bitwise_and(current_frame, current_frame,mask= red_free)
        
        #final = part1 + part2
        cv2.imshow("cloak", part1+part2)
        if cv2.waitKey(4)== ord('q'):
            break
cap.release()
cv2.destroyAllWindows()