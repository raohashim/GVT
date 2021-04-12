
#file=open('saveascii.txt', "w")
#'w' deletes exisiting file, 'a' appends

#file.write(bits[0]+bits[1])
#file.close()

#Reading in:
#file=open('saveascii.txt', "r")
#readbits=file.read()
#file.close()

print "writereadbits.py"
#---------------------------------

def writebinaryfile(filename, bitstring):
	#usage: writebitsfile('filename.bin', bitstring)
	#writes bitstring into binary file 'filename.bin'

	import numpy as np
	import struct

	#use unsigned Bytes ('B'),
	#converts stream of bits into stream of Bytes (groups of 8) represented as decimal integers:
	numbytes=len(bitstring)/8;
	Bytes=np.zeros(numbytes,dtype=int)
	for m in range(numbytes):
	   Bytes[m]=eval('0b'+bitstring[m*8:(m*8+8)])
	#packs the Bytes into a stream:
	s=struct.pack('B'*len(Bytes), *Bytes)
	#Write the stream "s" to file:
	file=open(filename, "w")
	#'w' deletes exisiting file, 'a' appends
	file.write(s)
	file.close()


def readbinaryfile(filename):
	#usage: bitstring=readbinaryfile('filename.bin')
	#reads binary data from file 'filename.bin' and converts it into a string of bits

	import struct
        import numpy as np

	file=open(filename, "r")
	#read the stream from file:
	readdata=file.read()
	#unpacks the stream into an array of Bytes (8 bits):
	Bytesread=struct.unpack('B'*len(readdata),readdata)
	#Convert bytes into binary string:
	bitstring='';
        for byte in Bytesread:
	   #create bit strin from byte:
	   bits=bin(byte)
	   #remove leading '0b' and fill up to 8 bits with leading zeros:
	   bits=bits[2:].zfill(8)
	   #append to bits to bitstring:
   	   bitstring=bitstring+bits

	return bitstring


def data2codestring(data):
	#usage: codestring=data2codestring( data)
	#takes 2 bit values in array "data" and returns the string of codewords
	
	import struct
	import numpy as np

	#sequence of integers (indices):
	#limit data to range of codebook (-8 to 7):
	data=np.clip(data,-8,7)
	#binary codebook, turns indices into binary codewords:
	codeword={0:'0000',1:'0001',2:'0010',3:'0011',4:'0100',5:'0101',6:'0110',7:'0111',-8:'1000',-7:'1001',-6:'1010',-5:'1011',-4:'1100',-3:'1101',-2:'1110',-1:'1111'}
	#start with empty string:
	codestring='';
	for value in data:
	   #append new codewords:
	   codestring=codestring+codeword[value]
	#print bits

        return codestring


def codestring2data(codestring):
	#Decoder:--------------------------------------
	#usage: data=codestring2data(codestring)
	#reads binary data from codestring and converts it into a stream of 2 bit
	#values returned in data.
	import struct
        import numpy as np
	
	#Bits decoder, decodes the indices from the binary codewords:
	decodeword={'0000':0,'0001':1,'0010':2,'0011':3,'0100':4,'0101':5,'0110':6,'0111':7,'1000':-8,'1001':-7,'1010':-6,'1011':-5,'1100':-4,'1101':-3,'1110':-2,'1111':-1}
	#convert sequence of Bytes into sequence of bits:
	numdata=len(codestring)/4;
        #converts groups of 4 bits into data:
	data=np.zeros(numdata,dtype=int)
	n=0;
        for i in range(numdata):
  	    #print "i= ", i
            data[n]=decodeword[codestring[(i*4):(4+i*4)]]
	    #print "data[n]= ", data[n]
            n+=1

	return data


#Testing:
if __name__ == '__main__':
   import numpy as np

   #emulation of an encoder, example data:
   data=np.array([7,5,3,-2,-1,0,1,-2,-1,0,1,-8,-7,-5])
   print "data= ", data
   filename='savebin.bin'
   codestring=data2codestring(data)
   print "codestring= ", codestring
   #write to binary file
   writebinaryfile(filename, codestring)
   
   #Emulation of a decoder:
   codestring=readbinaryfile(filename)
   dataread=codestring2data(codestring)
   print "dataread=", dataread


