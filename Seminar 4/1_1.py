import cv2
import numpy as np
import matplotlib.pyplot as plt

#Import Orignal Image
fig = cv2.imread('circles.jpg',0)
ro,co = fig.shape

#Image Resizing
N = 2
ds = np.zeros ((ro/N,co/N))
ds = fig [0::N,0::N]
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

#Computing FFT of Orignal
fig_fft = np.fft.fft2(fig)/255.0
fig_fft_abs = abs (fig_fft)/512.0
#Applying Mask to Orignal FFT
fig_m = fig_fft*MO
fig_m_abs = abs (fig_m)/512.0
#Taking IFFT of Orignal
fig_ifft = np.fft.ifft2(fig_m)
fig_ifft_abs = abs (fig_ifft)
#Downsampled of Filtered Orignal
ds_filt = fig_ifft_abs [0::N,0::N]

#Computing FFT of Resized
ds_fft = np.fft.fft2(ds)/255.0
ds_fft_abs = abs (ds_fft)/512.0

cv2.imshow ("Orignal",fig)
cv2.imshow ("Resized",ds)
cv2.imshow ("FFT of Orignal",fig_fft_abs)
cv2.imshow ("FFT of Resized",ds_fft_abs)
cv2.imshow("2DFFT After Mask", fig_m_abs) 
cv2.imshow("2DFFT Down After Mask", ds_m_abs)
cv2.imshow ("Filtered Orignal",fig_ifft_abs)
cv2.imshow ("Downsampled of Filtered",ds_filt) 
while(True):
	if cv2.waitKey(0) & 0xFF == ord('q'):
		break
		
cv2.destroyAllWindows
