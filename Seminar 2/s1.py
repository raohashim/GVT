import cv2

#Read and show Image
img = cv2.imread ('lena.jpg')
cv2.imshow ('Orignal', img)
print ("The shape of Image is ", img.shape)
#print the intensity of specific color at the specific pixel
a = img [10,10, :]
print("The pixel value for colored image at [10,10] is:")
print(a)
print("Its type is:")
print(type(a))

#To Convert Color image to Grayscale
Y=(0.114*img[:,:,0]+0.587*img[:,:,1]+0.299*img[:,:,2])/255; 

#Show Grayscale Image
cv2.imshow('Grayscale',Y)
b = Y [10,10]
print("The pixel value for colored image at [10,10] is:")
print(b)
print("Its type is:")
print(type(Y))
print ("Press 'q' to exit the program")
#For Ending 
while (True):
	if cv2.waitKey(0) & 0xFF == ord('q'):
		break

cv2.destroyAllWindows()


