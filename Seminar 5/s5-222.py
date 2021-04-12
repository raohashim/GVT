import cv2
import numpy as np
import scipy.fftpack as sft
import blockdct



#resulting quantization step size for 2^bits steps:
#Stufen fuer unterschiedliche Ortsfrequenzen:
bits=4
quantstufe1=5.0/(2**bits-1)
bits=3
quantstufe2=1.0/(2**bits-1)
bits=2
quantstufe3=0.6/(2**bits-1)
bits=1
quantstufe4=0.4/(2**bits-1)
bits=0
quantstufe5=8.0/(2**bits-0.99) #vermeide div. durch 0!
#Zus.: 1*4 bits + 2* 3 bits + 3*2bits + 4*1 bits fuer 64 pixel, also 0.3125 bit pro pixel!

#Quantisierungsstufen in "Maske", anti-diagonalen haben gleiche quantstufen:
M=np.zeros((8,8))
M[0,0]=quantstufe1
M=M+  np.fliplr(np.diag([1,1],6))*quantstufe2
M=M+  np.fliplr(np.diag([1,1,1],5))*quantstufe3
M=M+  np.fliplr(np.diag([1,1,1,1],4))*quantstufe4
M=M+  np.fliplr(np.tril(np.ones((8,8)),3))*quantstufe5

M=np.array([[16,11,10,16,24,40,51,61],
[12,12,14,19,26,58,60,55],
[14,13,16,24,40,57,69,56],
[14,17,22,29,51,87,80,62],
[18,22,37,56,68,109,103,77],
[24,35,55,64,81,104,113,92],
[49,64,78,87,103,121,120,101],
[72,92,95,98,112,100,103,99]])/64.0


print("Quantization Mask: \n", M)




def rgb2ycbcr(foto):


	b=foto[:,:,0]
	g=foto[:,:,1]
	r=foto[:,:,2]
	ycbcr=np.zeros(foto.shape)
	ycbcr[:,:,0] = .299*r + .587*g + .114*b
	ycbcr[:,:,1] = 128 -.168736*r -.331364*g + .5*b
	ycbcr[:,:,2] = 128 +.5*r - .418688*g - .081312*b

	return (ycbcr)

def ycbcr2rgb(ycbcr):

	rgb=np.zeros(ycbcr.shape)
	#ycbcr*=255
	y=ycbcr[:,:,0]
	cb=ycbcr[:,:,1]
	cr=ycbcr[:,:,2]
	rgb[:,:,2] = y + 1.402 * (cr-128)
	rgb[:,:,1] = y - .34414 * (cb-128)-  .71414 * (cr-128)
	rgb[:,:,0] = y + 1.772 * (cb-128)
        np.putmask(rgb, rgb > 255, 255)
        np.putmask(rgb, rgb < 0, 0)

	return (rgb)

#sub-sampling 4:2:0
def sample420(ycbcr):
	ds=np.zeros(ycbcr.shape)
	ds[0::,0::,0]=ycbcr[0::,0::,0]
	ds[0::2,0::2,1]=ycbcr[0::2,0::2,1]
	ds[1::2,1::2,2]=ycbcr[1::2,1::2,2]
	return(ds)


cap = cv2.VideoCapture(0)
#Get size of frame:
[retval, foto] = cap.read()
[r,c,d]=foto.shape
print(r,c)

cv2.imshow('original ', foto)

ycbcr=rgb2ycbcr(foto)
#cv2.imshow('ycbcr ', ycbcr/255)


ds=np.zeros(ycbcr.shape)
ds[::,::,0]=ycbcr[::,::,0]
ds[0::4,0::4,1]=ycbcr[0::4,0::4,1]
ds[0::4,0::4,2]=ycbcr[0::4,0::4,2]
#ds=sample420(ycbcr)
#cv2.imshow('sampled',ds/255)



#ds=sample420(ycbcr)
#rgb=ycbcr2rgb(ds)
#cv2.imshow('rgb420',rgb/255)


#Create quantization mask of the size of the image, using kronecker product:
r8=r//8
c8=c//8
Mframe=np.kron(np.ones((r8,c8)),M);

ycbcr1=np.zeros(ds.shape)





#compute the 2D DCT of blocks of 8x8 pixels of the green component, of normalized frame:
X=blockdct.dct8x8(ds[:,:,0]/255.0)
#Quantize:
#print('Quantisieren mit Quantisierungsmaske:')
indices=np.round(X/Mframe)
#print indices
#print('De-Quantisieren')
#de-quantization in the decoder:
Xrek=indices*Mframe
x=blockdct.invdct8x8(Xrek);
ycbcr1[:,:,0]=x

#compute the 2D DCT of blocks of 8x8 pixels of the green component, of normalized frame:
X=blockdct.dct8x8(ds[:,:,1]/255.0)
#Quantize:
#print('Quantisieren mit Quantisierungsmaske:')
indices=np.round(X/Mframe)
#print indices
#print('De-Quantisieren')
#de-quantization in the decoder:
Xrek=indices*Mframe
x=blockdct.invdct8x8(Xrek);
ycbcr1[:,:,1]=x


#compute the 2D DCT of blocks of 8x8 pixels of the green component, of normalized frame:
X=blockdct.dct8x8(ds[:,:,2]/255.0)
#Quantize:
#print('Quantisieren mit Quantisierungsmaske:')
indices=np.round(X/Mframe)
#print indices
#print('De-Quantisieren')
#de-quantization in the decoder:
Xrek=indices*Mframe
x=blockdct.invdct8x8(Xrek);
ycbcr1[:,:,2]=x


#cv2.imshow('X', ycbcr1)

rgb=ycbcr2rgb(ycbcr1*255)
cv2.imshow('re-ds', rgb/255)







cv2.waitKey(0)
cv2.destroyallwindows()


