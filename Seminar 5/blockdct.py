
import scipy.fftpack as sft
import numpy as np

#Forward 8x8 DCT of type 2, orthogonal:    
def dct8x8(frame):
   
    [r,c]=frame.shape

    frame=np.reshape(frame,(-1,8), order='C')
    X=sft.dct(frame,axis=1,norm='ortho')
    
    #shape it back to original shape:
    X=np.reshape(X,(-1,c), order='C')
    #Shape frame with columns of hight 8 by using transposition .T:
    X=np.reshape(X.T,(-1,8), order='C')
    X=sft.dct(X,axis=1,norm='ortho')
   
    #shape it back to original shape:
    X=(np.reshape(X,(-1,r), order='C')).T
    return X

 
#Inverse 2D DCT of type 2, orthogonal:
def invdct8x8(X):
    #Usage: x=invdct8x8(X)
    #with X: array of coefficients of 8x8 DCT's
    #x: reconstructed frame.

    #find the shape of 
    [r,c]=X.shape
    #Rows:
    X=np.reshape(X,(-1,8), order='C')
    X=sft.idct(X,axis=1,norm='ortho')
    #shape it back to original shape:
    X=np.reshape(X,(-1,c), order='C')
    #Shape frame with columns of hight 8 (columns: order='F' convention):
    X=np.reshape(X.T,(-1,8), order='C')
    x=sft.idct(X,axis=1,norm='ortho')
    #shape it back to original shape:
    x=(np.reshape(x,(-1,r), order='C')).T 
    return x

#Testing:
if __name__ == '__main__':
   import numpy as np

   frame=np.ones((16,16));
   print("frame= ", frame)
   X=dct8x8(frame)
   print("dct8x8(frame)= ", X);
   x=invdct8x8(X)
   print("reconstructed x: ", x)


