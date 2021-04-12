import cv2 
import numpy as np

cap=cv2.VideoCapture(0)
cv2.namedWindow("Orignal")
cv2.namedWindow("YCbCr")
cv2.namedWindow("RGB")
esc=True
y=0.5
x=0.5
c=0.5
def RGBtoYCbCR (ycbcr):
	YCbCr = np.empty_like(ycbcr)
	b = frame [:,:,0]
	g = frame [:,:,1]
	r = frame [:,:,2]
	# Converting image in to YCbCr formate using lecture fromula
	y=(0.299*r + 0.587*g + 0.114*b)/256
	cb= (-0.16*r - 0.33*g + 0.5*b +128)/256    
	cr= (0.5*r - 0.418*g - 0.081*b +128)/256
	#YCbCr [:,:,0] = cb
	#YCbCr [:,:,1] = y
	#YCbCr [:,:,2] = cr
	return (y,cb,cr)

def ycbcr2gbr (y,cb,cr):
	# Converting back from YCbCr to RGB
	#y,cb,cr = np.empty_like(YCbCr)	
	#cb = YCbCr [:,:,0]
	#y = YCbCr [:,:,1]
	#cr = YCbCr [:,:,2]
	R = y + 1.402*cr-190
	G = y - 0.344*cb+43.904
	B = y + 1.765*cb-225.92
	RGB [:,:,0] = B
	RGB [:,:,1] = G
	RGB [:,:,2] = R
	return(RGB)
	
while (True):
	[ret, frame]= cap.read()
	cv2.imshow ("Orignal", frame)
	[ret, ycbcr]= cap.read()
	g,h,j = RGBtoYCbCR (ycbcr)
	BGR = ycbcr2gbr (g,h,j)
	q = y*BGR[:,:,0]
	w = x*BGR[:,:,1]
	e = c*BGR[:,:,2]
	RGB = np.empty_like(BGR)
	RGB [:,:,0] = q  
	RGB [:,:,1] = w
	RGB [:,:,2] = e
	k = cv2.waitKey(1)
	k = k & 0xFF
	
	cv2.putText(RGB,"Press 'a' for increment in Blue and 'y' for decrement in Blue",(10,10),cv2.FONT_HERSHEY_SIMPLEX,0.4,(0,255,255))
	cv2.putText(RGB,"Press 's' for increment in Green and 'x' for decrement in Green",(10,20),cv2.FONT_HERSHEY_SIMPLEX,0.4,(0,255,255))
	cv2.putText(RGB,"Press 'd' for increment in Red and 'c' for decrement in Red",(10,30),cv2.FONT_HERSHEY_SIMPLEX,0.4,(0,255,255))
	cv2.putText(RGB,"Press 'esc' to reset the video Back to RGB",(10,40),cv2.FONT_HERSHEY_SIMPLEX,0.4,(0,0,0))
	cv2.putText(RGB,"Press 'q' to exit",(10,50),cv2.FONT_HERSHEY_SIMPLEX,0.4,(0,0,0))
	cv2.imshow ("YCbCr", YCbCr)
	cv2.imshow ("RGB", RGB)

	if k == ord('a'):
		y = y+0.1
	if k == ord('y'):
		y = y-0.1

	if k == ord('s'):
		x = x+0.1
	if k == ord('x'):
		x = x-0.1

	if k == ord('d'):
		c = c+0.1
	if k == ord('c'):
		c = c-0.1

	if k == 27:
		y=0.5
		x=0.5
		c=0.5	

	if k == ord('q'):
		break


	
cap.release()
cv2.destroyAllWindows()
