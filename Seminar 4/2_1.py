import scipy.signal
import cv2
import numpy as np

#Import Orignal Image
fig = cv2.imread('circles.jpg')
Y=(0.114*fig[:,:,0]+0.587*fig[:,:,1]+0.299*fig[:,:,2])/255;
ro,co = Y.shape
#Image Resizing
N = 2
ds = np.zeros ((ro/N,co/N))
ds = Y [0::N,0::N]
cv2.imshow("Downsampled Orignal", ds)
(rs,cs) = ds.shape

#Creating mask for Orignal Image
#for rows
Mro = np.ones((ro,1))
Mro[int(ro/8.0):int(ro - int(ro/8.0)),0] = np.zeros((int((3.0/4.0)*ro)))
#for columns
Mco = np.ones((1,co))
Mco[0,int(co/8.0):int(co - int(co/8.0))] = np.zeros((int((3.0/4.0)*co)))
#together
MO = np.dot(Mro,Mco)

#Inverse 2D Fourier transform of Low Pass filter for oringal Image:
IMO = np.abs(np.fft.ifft2(MO))
IMOC =np.concatenate((IMO[:,int(co/2):co], IMO[:,0:int (co/2)]), axis =1)
IMOC =np.concatenate((IMOC[int(ro/2):ro,:], IMOC[0:int (ro/2),:]))
#Only keep the piece with the biggest components:
IMOC = IMOC[int(ro/2-10):int(ro/2+10), int(co/2-10):int(co/2+10)]
Ofilt = IMOC
#Applying Mask to Orignal Image
Yfilt=scipy.signal.convolve2d(Y,Ofilt,mode='same')

# Display the resulting filtered frame
cv2.imshow('Y low-pass filtered',Yfilt*0.5)
cv2.imshow('Orignal Y ' , Y)

#Downsampled Masked Image
dy = Yfilt [0::N,0::N]
cv2.imshow('low-pass filtered Sub Sampled',dy*0.5)

while(True):
	if cv2.waitKey(0) & 0xFF == ord('q'):
		break

# When everything done, destroy all windows
cv2.destroyAllWindows()
