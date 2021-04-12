import cv2
import numpy
import matplotlib.pyplot as plt
import matplotlib.image as mpimg


# Read the image
pic =cv2.imread('lena.jpg')

# Convert the BGR image to YCrCb
B = pic[:, :, 0]
G = pic[:, :, 1]
R = pic[:, :, 2]

# /255 because the result is float values which imshow expects in range 0...1:
Y = ((R * 0.299)+ (G * 0.587) + (B * 0.114))/255
Cr= (128 +((0.5*B)-(0.16876*R)-(0.331264*G)))/255
Cb= (128 +(0.5*R)-(0.418688*G)-(0.081312*B))/255

pic_YCrCb=numpy.zeros(pic.shape)
pic_YCrCb[:,:,0]=Y
pic_YCrCb[:,:,1]=Cr
pic_YCrCb[:,:,2]=Cb

# Show the image conversion

cv2.imshow('Color Pic', pic)
cv2.imshow('YCrCb', pic_YCrCb)


# 4:2:2 Color Subsampling
CbDown=numpy.zeros(Cb.shape)
CbDown[:,0::2]=Cb[:,0::2]
cv2.imshow('Cb Down 4:2:2', CbDown)

CrDown=numpy.zeros(Cr.shape)
CrDown[:,0::2]=Cr[:,0::2]
cv2.imshow('Cr Down 4:2:2', CrDown)

cv2.imshow('Y', Y)

print('CbDown', CbDown)
print('CrDown', CrDown)
print('Y', Y)

#4:2:0 Color Subsampling
CbDown0=numpy.zeros(Cb.shape)
CbDown0[0::2,0::2]=Cb[0::2,0::2]
cv2.imshow('Cb Down 4:2:0', CbDown0)

CrDown0=numpy.zeros(Cr.shape)
CrDown0[:,0::2]= Cr[:,0::2]
cv2.imshow('Cr Down 4:2:0', CrDown0)


print('CbDown0', CbDown0)
print('CrDown0', CrDown0)

# Display the image for specified miliseconds
cv2.waitKey(0)      
cv2.destroyAllWindows()
