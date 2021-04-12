import cv2 as c

cap = c.VideoCapture(0)

c.namedWindow("test")

print (" Press 'q'to terminate the program OR Press 'Spacebar' to capture frame")

while (True):

    (retval, frame) = cap.read() #Read the frame
    c.imshow("test", frame) #Show the frame
    
    k = c.waitKey(1) #assigning cv2.waitkey () to variable k
    

    if k % 0xFF == ord ('q'):
        # q pressed
        print("q hit, closed...")
        break
    elif k % 0xFF == ord (' '):
        # SPACE pressed
        img = "Pic.jpg" # Create a file 
        c.imwrite(img, frame) # save the current frame to the file
	photo=c.imread('Pic.jpg')#read the captured image
	c.imshow('Captured Webcam Shot',photo)#Show the captured image
        
cap.release()

c.destroyAllWindows()
