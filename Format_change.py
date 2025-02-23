import cv2

img=cv2.imread("Nature.jpg")
cv2.imshow("Image1",img)
cv2.imwrite("Nature.png",img)
cv2.waitKey(5000)
cv2.destroyAllWindows()
