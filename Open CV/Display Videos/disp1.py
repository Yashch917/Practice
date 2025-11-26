import cv2
vid=cv2.VideoCapture(r"C:\Users\HP\OneDrive\Desktop\daad\Practice\Open CV\Display Videos\vid.mp4")
while True:
    ret,frame=vid.read()
    if ret==False:
        break
    cv2.imshow("Video Frame",frame)
    if cv2.waitKey(25) & 0xFF==ord('q'):
        break
vid.release()
cv2.destroyAllWindows()