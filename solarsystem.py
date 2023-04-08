import cv2


img = cv2.imread("solar-system.jpg")


cv2.putText(img, "Sun" ,(50, 200), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
cv2.putText(img, "Mercury", (60, 370), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)
cv2.putText(img, "Venus", (140, 310), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)
cv2.putText(img, "Earth", (250, 280), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)
cv2.putText(img, "Mars", (370, 300), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)
cv2.putText(img, "Jupiter", (500, 270), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)
cv2.putText(img, "Saturn", (660, 280), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)
cv2.putText(img, "Uranus", (820, 280), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)
cv2.putText(img, "Neptune", (940, 280), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)


cv2.imshow("output", img)


cv2.waitKey(0)
cv2.destroyAllWindows()


cv2.imwrite("Solar_systemwithname.jpg", img)
