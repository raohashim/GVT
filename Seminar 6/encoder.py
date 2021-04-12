#Program to capture a video from the default camera (0), compute the 2D DCT 
#on the Y, Cr, CB component, quantize the lowest 3 coefficients of each DCT block and save them as 2 bit values in files framedimc.txt, y00encc.bin, u00enc.bin, v00enc.bin y01encc.bin, and y10encc.bin
#Gerald Schuller, Dec. 2015

import cv2
import numpy as np
import scipy.fftpack as sft
#import our file functions:
from writereadbits import *
import blockdct


cap = cv2.VideoCapture(0)
#Get size of frame:
[retval, frame] = cap.read()
[r,c,d]=frame.shape
print(r,c)
#Store dimensions in info file:
np.savetxt('framedimc.txt', [r,c])

print "Record to compressed files with key 'c', show until key 'q' is pressed "

N=8;

while(True):
    # Capture frame-by-frame
    [retval, frame] = cap.read()    

    # /256 because the result is float values which imshow expects in range 0...1:
    Y=(0.114*frame[:,:,0]+0.587*frame[:,:,1]+0.299*frame[:,:,2])/255;        
    #U=B-Y:
    U=frame[:,:,0]/255.0-Y;
    #V=R-Y:
    V=frame[:,:,2]/255.0-Y;
    
    key=cv2.waitKey(1) & 0xFF
    if key== ord('c'):
        print("store frame encoded in files framedimc.txt, y00encc.bin, y01encc.bin, y10encc.bin, y20encc.bin, y11encc.bin, y02encc.bin, u00enc.bin,u01enc.bin,u10enc.bin, v00enc.bin, v01enc.bin,v10enc.bin")

        #compute magnitude of 2D DCT of blocks of 8x8 pixels of theY component
        Ydct=blockdct.dct8x8(Y)
        Udct=blockdct.dct8x8(U)
        Vdct=blockdct.dct8x8(V)
        
        bitsdc=4
	bitsac=2

        #resulting quantization step size for 2^bits steps:
        #DC Indices mit range 0...5:
        #quantstufeDC=5.0/(2**bitsdc-1)

        #Alle DC indices (anfangen mit Position 0 und dann jeder N'te Koeffizient:
        #Kleinsten Indexwert addieren um den ganzen range des coders zu nutzen:
	print ("YDCT max and min", np.max(Ydct[0::N,0::N]),np.min(Ydct[0::N,0::N]))
        indices00=np.round(Ydct[0::N,0::N]/(2**bitsdc-1))-8
	print ("Indices00" , np.max(indices00), np.min(indices00)) 
        #reshape into 1-D array:
        indices00=np.reshape(indices00,(1,-1))
        #print indices00.shape
        #convert to code string:
        codestring00=data2codestring(indices00[0,:])
        #write  to binary file
        writebinaryfile('y00encc.bin', codestring00)


        #Zwei AC Koeffizienten, mit range 0.5-(-0.5)
        #DCT Koeffizienten der Position (0,1):
        quantstufeAC=1.0/(2**bitsac-1)
        indices01=np.round(Ydct[0::N,1::N]/quantstufeAC)
	print ("Indices01" , np.max(indices01), np.min(indices01)) 
        #Reshape:
        indices01=np.reshape(indices01,(1,-1))
        #Store with 2 bits each value:
        #convert to code string:
        codestring01=data2codestring(indices01[0,:])
        #write to binary file
        writebinaryfile('y01encc.bin', codestring01)

        #DCT Koeffizienten der Position (1,0):
        indices10=np.round(Ydct[1::N,0::N]/quantstufeAC)
        print ("Indices10" , np.max(indices10), np.min(indices10))
	indices10=np.reshape(indices10,(1,-1))
	 
        #convert to code string:
        codestring10=data2codestring(indices10[0,:])
        #write to binary file
        writebinaryfile('y10encc.bin', codestring10)

        #DCT Koeffizienten der Position (2,0):
        indices20=np.round(Ydct[2::N,0::N]/quantstufeAC)
	print ("Indices20" , np.max(indices20), np.min(indices20))
        indices20=np.reshape(indices10,(1,-1))
        #convert to code string:
        codestring10=data2codestring(indices10[0,:])
        #write to binary file
        writebinaryfile('y20encc.bin', codestring10)

        #DCT Koeffizienten der Position (1,1):
        indices11=np.round(Ydct[1::N,1::N]/quantstufeAC)
	print ("Indices11" , np.max(indices11), np.min(indices11))
        indices11=np.reshape(indices10,(1,-1))
        #convert to code string:
        codestring11=data2codestring(indices10[0,:])
        #write to binary file
        writebinaryfile('y11encc.bin', codestring10)

        #DCT Koeffizienten der Position (0,2):
        indices01=np.round(Ydct[0::N,2::N]/quantstufeAC)
        #Reshape:
        indices01=np.reshape(indices01,(1,-1))
        #Store with 2 bits each value:
        #convert to code string:
        codestring01=data2codestring(indices01[0,:])
        #write to binary file
        writebinaryfile('y02encc.bin', codestring01)
            
        #store color components DC Value:
        #DC Indices mit range 0...5:
        quantstufeDC=5.0/(2**bitsdc-1)
        #kleinsten Wert addieren...
        indicesU00=np.round(Udct[0::N,0::N]/quantstufeDC)
        #reshape into 1-D array:
        indicesU00=np.reshape(indicesU00,(1,-1))
        #print indices00.shape
        #convert to code string:
        codestringU00=data2codestring(indicesU00[0,:])
        #write  to binary file
        writebinaryfile('u00enc.bin', codestringU00)

        #DCT Koeffizienten der Position (0,1):
        quantstufeAC=1.0/(2**bitsac-1)
        #kleinsten Wert addieren...
        indicesU00=np.round(Udct[0::N,1::N]/quantstufeAC)
        #reshape into 1-D array:
        indicesU00=np.reshape(indicesU00,(1,-1))
        #print indices00.shape
        #convert to code string:
        codestringU00=data2codestring(indicesU00[0,:])
        #write  to binary file
        writebinaryfile('u10enc.bin', codestringU00)

        #DCT Koeffizienten der Position (1,0):
        #kleinsten Wert addieren...
        indicesU00=np.round(Udct[1::N,0::N]/quantstufeAC)
        #reshape into 1-D array:
        indicesU00=np.reshape(indicesU00,(1,-1))
        #print indices00.shape
        #convert to code string:
        codestringU00=data2codestring(indicesU00[0,:])
        #write  to binary file
        writebinaryfile('u01enc.bin', codestringU00)

        #Kleinsten Indexwert addieren um den ganzen range des coders zu nutzen:
        indicesV00=np.round(Vdct[0::N,0::N]/quantstufeAC)
        #reshape into 1-D array:
        indicesV00=np.reshape(indicesV00,(1,-1))
        #print indices00.shape
        #convert to code string:
        codestringV00=data2codestring(indicesV00[0,:])
        #write  to binary file
        writebinaryfile('v00enc.bin', codestringV00)

        #DCT Koeffizienten der Position (0,1):
        indicesV00=np.round(Vdct[0::N,1::N]/quantstufeAC)
        #reshape into 1-D array:
        indicesV00=np.reshape(indicesV00,(1,-1))
        #print indices00.shape
        #convert to code string:
        codestringV00=data2codestring(indicesV00[0,:])
        #write  to binary file
        writebinaryfile('v10enc.bin', codestringV00)

        #DCT Koeffizienten der Position (1,0):
        indicesV00=np.round(Vdct[1::N,0::N]/quantstufeAC)
        #reshape into 1-D array:
        indicesV00=np.reshape(indicesV00,(1,-1))
        #print indices00.shape
        #convert to code string:
        codestringV00=data2codestring(indicesV00[0,:])
        #write  to binary file
        writebinaryfile('v01enc.bin', codestringV00)

    cv2.putText(frame,"Frame Compression Demo,", (20,50), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255,128,128))
    cv2.putText(frame,"Press 'c' to take picture, 'q' to quit,", (20,80), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255,128,128))
    cv2.imshow('Original Video, Y Komponente, 8bits/Pixel',frame)	    
    #Keep window open until key 'q' is pressed:
    if  key == ord('q'):
        break
# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()

