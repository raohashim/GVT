import numpy as np
import copy as cp
#formation of 3D array
x= np.random.randint(0, 50, size = (100, 100, 100))
print(x)
#to copy into variable y
y=cp.copy(x)
print('This value of y is:' , y)
#For Slicing of the second row
print('The second row of y is:', y[1,1,:])
#for specific element 
z=y[1,1,2]
print("The sliced of second row is:", z)

