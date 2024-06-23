import cv2 #cv2 module of opencv-python
#configurable parameters
source = "IMG_3412.JPG"
destinatiom = "newimage4.jpg"
scale_percent = 90 #percent by which image is resized

image = cv2.imread(source,cv2.IMREAD_UNCHANGED)
cv2.imshow("title",image)

#calculate the new height and width
new_width = int(image.shape[1] * scale_percent/100) #width shape[1]
new_height = int(image.shape[0] * scale_percent/100) #height shape[0]

output = cv2.resize(image,(new_width,new_height)) #resize function

cv2.imwrite(destinatiom,output)
cv2.waitKey((0))

