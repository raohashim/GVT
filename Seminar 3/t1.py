import cv2
import numpy as np

image = cv2.imread('lena.jpg')
cv2.imshow('Original',image)
print("The shape of image is : ", image.shape)
N=2
image_converted=np.empty_like(image)
r=image[:,:,2]
g=image[:,:,1]
b=image[:,:,0]

y= (0.299*r + 0.587*g + 0.114*b)/256
cb=(-0.16*r - 0.33*g + 0.5*b +128)/256    
cr= (0.5*r - 0.418*g - 0.081*b +128)/256
cv2.imshow ('Y', y)
cv2.imshow('Cb', cb)
cv2.imshow ('Cr', cr)
cb22=np.zeros(cb.shape)
cr22=np.zeros(cr.shape)   

cb22[0::N,0::N]=cb[0::N,0::N]
cr22[0::N,0::N]=cr[0::N,0::N]

#cb20=np.zeros(cb.shape)
#cr20=np.zeros(cr.shape)
#cb20[1::N,1::N]=0
#cr20[1::N,1::N]=0

image_converted[:,:,0]=cr22
image_converted[:,:,1]=cb22
image_converted[:,:,2]=y

cv2.imshow('Cb22', cb22)
cv2.imshow ('Cr22', cr22)
	
#y=image_converted[:,:,2]
#cb1=image_converted[:,:,1]
#cr1=image_converted[:,:,0]

#used	
r = y + 1.402*cr-190
g = y - 0.344*cb+43.904
b = y + 1.765*cb-225.92
#end
image_converted2=np.empty_like(image)
image_converted2[:,:,2] = r
image_converted2[:,:,1] = g
image_converted2[:,:,0] = b

cv2.imshow('YCbCr22',image_converted)
cv2.imshow('RGB',image_converted2)	

p=image_converted2

a=p[256:260:,256:260:]
dim = (512, 512) 
# perform the actual resizing of the image and show it
resized = cv2.resize(a, dim, interpolation = cv2.INTER_AREA)
print (" The shape of resized image is :", resized.shape)
cv2.imshow("resized", resized)

cv2.waitKey(0)
while(True):
	k = cv2.waitKey(50)
	if k & 0xFF == ord('q'):
		break

cv2.destroyAllWindows()
		
	


