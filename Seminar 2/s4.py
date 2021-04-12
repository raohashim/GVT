import cv2 as c
import numpy as np

#read the image and show it
ima = c.imread('lena.jpg')
c.imshow ('o', ima)
print (" The shape of imported image is ", ima.shape)
photo422=np.empty_like(ima)
photo420=np.empty_like(ima)
RGB=np.empty_like(ima)
N = 4

#Assigning BGR components of picture to variables
b = ima [:,:,0]
g = ima [:,:,1]
r = ima [:,:,2]

# Converting image in to YCbCr formate using lecture fromula
y = ((r * 0.299)+ (g * 0.587) + (b * 0.114))
cr= (128 +((0.5*b)-(0.16876*r)-(0.331264*g)))
cb= (128 +(0.5*r)-(0.418688*g)-(0.081312*b))
c.imshow ('Y', y)# Show Luminance
c.imshow ('Cb', cb)# Show Cb
c.imshow ('Cr', cr)# Show Cr

#Creating a matrix of Zeros
cb422 = np.zeros(cb.shape)
cr422 = np.zeros(cr.shape)
cb420 = np.zeros(cb.shape)
cr420 = np.zeros(cr.shape)

#For 4:2:2 downsampling
cb422[:,0::N] = cb[:,0::N]
#print ('the cb422 is' , cb422)
#c.imshow ('Cb422', cb422)
cr422[:,0::N] = cr[:,0::N]
print ('the cr422 is' , cr422)
#c.imshow ('Cr422', cr422)

#For 4:2:0 downsampling
cb420[0::N,0::N] = cb[0::N,0::N]
#print ('the cb422 is' , cb420)
#c.imshow ('Cb420', cb420)
cr420[0::N,0::N] = cr[0::N,0::N]
#print ('the cr422 is' , cr420)
#c.imshow ('Cr420', cr420)

#Back from YCbCr to RGB
R = (y+1.402*(cr-128))
#print R
G = (y - (0.344136*(cb-128))-(0.714136*(cr-128)))
#print G
B = y+ (1.722 * (cb-128))
#print B
RGB [:,:,0] = B
RGB [:,:,1] = G
RGB [:,:,2] = R
c.imshow ('RGB', RGB)
#Closing Loop
while (True):
	if c.waitKey(0) & 0xFF == ord('q'):
		break

c.destroyAllWindows()

