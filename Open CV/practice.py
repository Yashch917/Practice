#display three images with different window names
import cv2
img=cv2.imread(r"C:\Users\HP\OneDrive\Desktop\daad\Practice\Open CV\Images\wertyuiop.jpg")
cv2.imshow("Image 1",img)
img=cv2.imread(r"C:\Users\HP\OneDrive\Desktop\daad\Practice\Open CV\Images\asdfgh (1).jpg")
cv2.imshow("Image 2",img)
img=cv2.imread(r"C:\Users\HP\OneDrive\Desktop\daad\Practice\Open CV\Images\asdfgh (2).jpg")
cv2.imshow("Image 3",img)
img=cv2.imread(r"C:\Users\HP\OneDrive\Desktop\daad\Practice\Open CV\Images\asdfgh (3).jpg")
cv2.imshow("Image 4",img)
cv2.waitKey(0)
cv2.destroyAllWindows()