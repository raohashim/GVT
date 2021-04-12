import numpy as np

def	myfunction(a,b):
	
	A= np.array([[4,7],[6,0]])
	B= np.array([[a,b],[7,1]])
	
	W = A + B
	print('Addition..', W)
	
	X = A * B
	print('Multiplication..', X)

	Y = np.multiply(A,B)
	print('Element Multiplication..', Y)

	Z = np.linalg.inv(A)
	print('Inverse..', Z)
	
	a = int ( input ("please enter value of a: "))
        print ("Value of a is : ", str(a))
	b= int ( input("please enter the value of b: "))
	print ("Value of b is : " , str(b))

	myfunction(a,b)

	result=open("./Desktop/arrayResult.txt", "w");
	result.write(" ADD : " + str(W) + " \n\n Multiply : "+ str(X) + 
	"\n\n Element Multiplication : " + str(Y) + "\n\n Inverse : " + str(Z));
	result.close;
	return ()

