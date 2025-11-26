import cv2
img1=cv2.imread(r"C:\Users\HP\OneDrive\Desktop\daad\Practice\Open CV\Display Images\Images\wertyuiop.jpg")
img2=cv2.imread(r"C:\Users\HP\OneDrive\Desktop\daad\Practice\Open CV\Display Images\Images\asdfgh (1).jpg")
img3=cv2.imread(r"C:\Users\HP\OneDrive\Desktop\daad\Practice\Open CV\Display Images\Images\asdfgh (2).jpg")
img4=cv2.imread(r"C:\Users\HP\OneDrive\Desktop\daad\Practice\Open CV\Display Images\Images\asdfgh (3).jpg")

img1=cv2.resize(img1,(500,200))
img2=cv2.resize(img2,(500,200))
img3=cv2.resize(img3,(500,200))
img4=cv2.resize(img4,(500,200))

combined=cv2.vconcat([img1,img2,img3,img4])
cv2.imshow("Combined Image",combined)
cv2.waitKey(0)
cv2.destroyAllWindows()