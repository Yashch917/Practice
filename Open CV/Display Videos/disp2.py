import cv2
vid=cv2.VideoCapture(r"C:\Users\HP\OneDrive\Desktop\daad\Practice\Open CV\Display Videos\vid.mp4")
vid1=cv2.VideoCapture(r"C:\Users\HP\OneDrive\Desktop\daad\Practice\Open CV\Display Videos\vid1.mp4")

while True:
    ret,frame=vid.read()
    ret1,frame1=vid1.read()
    if not ret or not ret1:
        break
    frame=cv2.resize(frame,(500,400))
    frame1=cv2.resize(frame1,(500,400))
    combined1=cv2.hconcat([frame,frame1])
    cv2.imshow("Video Frame",combined1)
    if cv2.waitKey(25) & 0xFF==ord('q'):
        break

vid.release()
vid1.release()
cv2.destroyAllWindows()