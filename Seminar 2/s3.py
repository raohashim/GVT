import cv2 as c
import numpy as np

#read the image and show it
ima = c.imread('lena.jpg')
c.imshow ('o', ima)
print ima.shape
photo422=np.empty_like(ima)
photo420=np.empty_like(ima)
N = 4

#Assigning BGR components of picture to veriables
B = ima [:,:,0]
G = ima [:,:,1]
R = ima [:,:,2]

# Converting image in to YCbCr formate using lecture fromula
#y = 0.299*r + 0.587*g + 0.114*b
#cb = 128 - 0.168736*r - 0.331264*g + 0.5*b     
#cr = 128 + 0.5*r - 0.418688*g - 0.081312*b 
y = ((R * 0.299)+ (G * 0.587) + (B * 0.114))/255
cr= (128 +((0.5*B)-(0.16876*R)-(0.331264*G)))/255
cb= (128 +(0.5*R)-(0.418688*G)-(0.081312*B))/255
c.imshow ('Y' , y)
c.imshow ('Cb' , cb)
c.imshow ('Cr' , cr)
#Assigning variable for 4:2:0 sampling
cb420 = cb.copy()
cr420 = cr.copy()

#Assigning variable for 4:2:2 sampling
cb422 = cb.copy()
cr422 = cr.copy()

#Creating a matrix of Zeros
cbz = np.zeros(cb.shape)

#For 4:2:2 downsampling
cb422[::,1::N] = cbz[::,1::N]
print cb422
cr422[::,1::N] = cbz[::,1::N]
print cr422

#For 4:2:0 downsampling
cb420[1::N,1::N] = cbz[1::N,1::N]
print cr420
cr420[1::N,1::N] = cbz[1::N,1::N]
print cr420

# Downsampled Photo 4:2:2
photo422[:,:,0]=y
photo422[:,:,1]=cb422
photo422[:,:,2]=cr422

# Downsampled Photo 4:2:0
photo420[:,:,0]=y
photo420[:,:,1]=cb420
photo420[:,:,2]=cr420

#Show the downsampled Photos
c.imshow('4:2:2 Chroma Sampled Lena',photo422)
c.imshow('4:2:0 Chroma Sampled Lena',photo420)

#Saving the Desampled Photo
c.imwrite('lena 4:2:2.jpg',photo422)
c.imwrite('lena 4:2:0.jpg',photo420)

#Closing Loop
while (True):
	if c.waitKey(0) & 0xFF == ord('q'):
		break

c.destroyAllWindows()

