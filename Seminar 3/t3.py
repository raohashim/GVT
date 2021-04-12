import cv2
import numpy as np
N = 2
fig = cv2.imread ('circles.jpg')
cv2.imshow ('Orignal', fig)
[rows,columns,c]=fig.shape
print (" THe shape of Image is ", rows,columns,c)

rs = np.zeros ((rows/N , columns/N))
rs = fig [0::N,0::N]
cv2.imshow ('Converted' , rs)
[r,cl,c]=rs.shape
print (" The resolution of resized image is : ", r,cl,c)

while(True):
	if cv2.waitKey(0) & 0xFF == ord('q'):
		break
		
cv2.destroyAllWindows
