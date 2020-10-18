import cv2
import numpy as np
import pyautogui

screen_size = (1920,1080)

fourcc = cv2.VideoWriter_fourcc(*"XVID") 
# "XVID" is the codecc used here. use *"mp4v" codecc for mp4 files.

out = cv2.VideoWriter("output.avi", fourcc, 14.0, (screen_size))
flag = 0

# Create an Empty window 
cv2.namedWindow("Live", cv2.WINDOW_NORMAL) 
  
# Resize this window 
cv2.resizeWindow("Live", 480, 270) 

while True:
    # make a screenshot
    img = pyautogui.screenshot()
    # img = pyautogui.screenshot(region=(0, 0, 300, 400))

    # convert these pixels to a proper numpy array to work with OpenCV
    frame = np.array(img)

    # convert colors from BGR to RGB
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # write the frame
    out.write(frame)

    # show the frame
    #cv2.imshow("Live", frame)
        
    # if the user clicks q, it exits
    if cv2.waitKey(1) == ord("q"):
        break

# make sure everything is closed when exited
cv2.destroyAllWindows()
out.release()