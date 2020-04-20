import numpy as np
import cv2
def click(event,x,y,flag,param):
    if event==cv2.EVENT_LBUTTONDOWN:
        font=cv2.FONT_HERSHEY_COMPLEX
        frame=np.zeros([720,1200,3],np.uint8)
        cv2.putText(frame,'X='+str(x)+',',(x,y),font,0.5,(255,255,255),1,cv2.LINE_AA)
        cv2.putText(frame,'Y='+str(y),(x+60,y),font,0.5,(255,255,255),1,cv2.LINE_AA)
        cv2.imshow("komal",frame)
frame=np.zeros([720,1200,3],np.uint8)
cv2.imshow('komal',frame)
cv2.setMouseCallback('komal',click)
cv2.waitKey(0)
cv2.destroyAllWindows()
