import cv2

img = cv2.imread("solar-system.jpg")
cv2.putText(img,  
           "sun",
           (100, 80),  
           fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,
           fontScale=2,  
           color=(0,0,255)
           )
cv2.putText(img,  
           "mercury",
           (110, 180),  
           fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,
           fontScale=0.5,  
           color=(0,0,255)
           )
cv2.putText(img,  
           "venus",
           (190, 270),  
           fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,
           fontScale=0.5,  
           color=(0,0,255)
           )
cv2.putText(img,  
           "earth",
           (300, 270),  
           fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,
           fontScale=0.5,  
           color=(0,0,255)
           )
cv2.putText(img,  
           "mars",
           (400, 270),  
           fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,
           fontScale=0.5,  
           color=(0,0,255)
           )
cv2.putText(img,  
           "jupiter",
           (500, 90),  
           fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,
           fontScale=0.5,  
           color=(0,0,255)
           )
cv2.putText(img,  
           "saturn",
           (720, 110),  
           fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,
           fontScale=0.5,  
           color=(0,0,255)
           )
cv2.putText(img,  
           "uranus",
           (950, 130),  
           fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,
           fontScale=0.5,  
           color=(0,0,255)
           )
cv2.putText(img,  
           "neptune",
           (1080, 130),  
           fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,
           fontScale=0.5,  
           color=(0,0,255)
           )
cv2.imshow("output",img)
cv2.waitkey(0)
cv2.imwrite("solar_system.jpg",img)
