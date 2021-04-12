#Program to decode a color video from files framedimc.txt, y00encc.bin, y01encc.bin, and y10encc.bin, u00enc.bin, v00enc.bin
# using 2-bit DCT coefficient values
#Gerald Schuller, Dec. 2015


import cv2
import numpy as np
import scipy.fftpack as sft
#import our file functions:
from writereadbits import *
import blockdct

N=8;

#Read DC values of the DCT's from file:
#indices00=readbitsfile('y00enc.bin')
codestring00=readbinaryfile('y00encc.bin')
indices00=codestring2data(codestring00)
#Subtract smallest index value to obtain original value range:
indices00=indices00+8;
#Read AC values from file:
#indices01=readbitsfile('y01enc.bin')
codestring01=readbinaryfile('y01encc.bin')
indices01=codestring2data(codestring01)

#indices10=readbitsfile('y10enc.bin')
codestring10=readbinaryfile('y10encc.bin')
indices10=codestring2data(codestring10)

codestring20=readbinaryfile('y20encc.bin')
indices20=codestring2data(codestring20)

codestring11=readbinaryfile('y11encc.bin')
indices11=codestring2data(codestring11)

codestring02=readbinaryfile('y02encc.bin')
indices02=codestring2data(codestring02)

#Read in DC color components:
#indices00=readbitsfile('y00enc.bin')
codestringu00=readbinaryfile('u00enc.bin')
indicesu00=codestring2data(codestringu00)
#Subtract smallest index value to obtain original value range:
indicesu00=indicesu00;


codestringu01=readbinaryfile('u01enc.bin')
indicesu01=codestring2data(codestringu01)

codestringu10=readbinaryfile('u10enc.bin')
indicesu10=codestring2data(codestringu10)

#indices00=readbitsfile('y00enc.bin')
codestringv00=readbinaryfile('v00enc.bin')
indicesv00=codestring2data(codestringv00)
#Subtract smallest index value to obtain original value range:
#indicesv00=indicesv00;

codestringv01=readbinaryfile('v01enc.bin')
indicesv01=codestring2data(codestringv01)

codestringv10=readbinaryfile('v10enc.bin')
indicesv10=codestring2data(codestringv10)

#Reshape back into 2-D frame with rindex rows and cindex solumns:
#load dimensions from info file:
[r,c]=np.loadtxt('framedimc.txt')
r=int(r)
c=int(c)
rindex=int(r/8);
cindex=int(c/8);

indices00=np.reshape(indices00,(-1,cindex))
indices01=np.reshape(indices01,(-1,cindex))
indices10=np.reshape(indices10,(-1,cindex))
indices20=np.reshape(indices20,(-1,cindex))
indices11=np.reshape(indices11,(-1,cindex))
indices02=np.reshape(indices02,(-1,cindex))
#color components:
indicesu00=np.reshape(indicesu00,(-1,cindex))
indicesu01=np.reshape(indicesu01,(-1,cindex))
indicesu10=np.reshape(indicesu10,(-1,cindex))

indicesv00=np.reshape(indicesv00,(-1,cindex))
indicesv01=np.reshape(indicesv01,(-1,cindex))
indicesv10=np.reshape(indicesv10,(-1,cindex))

#print('De-Quantisieren')
#de-quantization in the decoder:
Ydct=np.zeros((r,c));
Udct=np.zeros((r,c));
Vdct=np.zeros((r,c));

#Number of bits per pixel
bitsdc=4
bitsac=2
#resulting quantization step size for 2^bits steps:
#Stufen fuer unterschiedliche Ortsfrequenzen:
#DC Indices mit range 0...5:
quantstufeDC=5.0/(2**bitsdc-1)
#Zwei AC Koeffizienten, mit range 0.5-(-0.5) 
quantstufeAC=1.0/(2**bitsac-1)

#DC values de-quantization:
Ydct[0::N,0::N]=indices00*quantstufeDC
#2 AC values de-quantization:
Ydct[0::N,1::N]=indices01*quantstufeAC
Ydct[1::N,0::N]=indices10*quantstufeAC
Ydct[2::N,0::N]=indices20*quantstufeAC
Ydct[1::N,1::N]=indices11*quantstufeAC
Ydct[0::N,2::N]=indices02*quantstufeAC
#The rest of the DCT coefficients is not transmitted and set to zero.

#color components de-quatization:
#DC Indices mit range 0...1:
quantstufeDC=5.0/(2**bitsdc-1)
#DC values de-quantization:
Udct[0::N,0::N]=indicesu00*quantstufeDC
Udct[0::N,1::N]=indicesu01*quantstufeAC
Udct[1::N,0::N]=indicesu10*quantstufeAC

Vdct[0::N,0::N]=indicesv00*quantstufeDC
Vdct[0::N,1::N]=indicesv01*quantstufeAC
Vdct[1::N,0::N]=indicesv01*quantstufeAC

#Inverse 2D DCT:
Y=blockdct.invdct8x8(Ydct)
U=blockdct.invdct8x8(Udct)
V=blockdct.invdct8x8(Vdct)

B=U+Y
R=V+Y
G=(Y-0.114*B-0.299*R)/0.587;
#Schreibe die RGB Komponenten in den rekonstruierten Frame: 
framerec=np.zeros((r,c,3));
framerec[:,:,0]=B;
framerec[:,:,1]=G;
framerec[:,:,2]=R;

#Store decoded picture in file "decodedpic.jpg":
cv2.imwrite('decodedpic.jpg', framerec*255)

while(True): 
    cv2.imshow('Decoder mit De-Quantizer und Inverse 2D DCT, mit 0.095 bits/Pixel! ', framerec)
    
    #Keep window open until key 'q' is pressed:
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
# When everything done, release the capture

cv2.destroyAllWindows()
