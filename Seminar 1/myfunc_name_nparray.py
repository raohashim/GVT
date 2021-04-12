import numpy as np

def	mymatrix(a,b):

	A= np.matrix([[4,7],[6,0]])
	B= np.matrix([[a,b],[7,1]])
	
	W = A + B
	print('Addition..', W)
	
	X = A * B
	print('Multiplication..', X)

	Y = np.multiply(A,B)
	print('Element Multiplication..', Y)

	Z = A.I
	print('Inverse..', Z)

	result=open("./Desktop/matrixResult.txt", "w");
	result.write(" ADD : " + str(W) + " \n\n Multiply : "+ str(X) + 
	"\n\n Element Multiplication : " + str(Y) + "\n\n Inverse : " + str(Z));
	result.close;
	return ()

