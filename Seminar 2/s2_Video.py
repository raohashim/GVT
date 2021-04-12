import cv2 as c

cap = c.VideoCapture(0)

c.namedWindow("test")

counter = 0

print (" Press 'q'to terminate the program OR Press 'Spacebar' to capture frame")

while (True):

    (retval, frame) = cap.read()#Read the frame
    c.imshow("test", frame)#Show the frame
    
    k = c.waitKey(1) #assigning cv2.waitkey () to variable k
    

    if k % 0xFF == ord ('q'):
        # q pressed
        print("q hit, closed...")
        break
    elif k % 0xFF == ord (' '):
        # SPACE pressed
        img = "Pic{}.png".format(counter) # Create a file 
        c.imwrite(img, frame) # save the current frame to the file
        print("{} Captured".format(img)) # Show the created file name 
 	counter += 1 # add 1 to counter for next file

cap.release()

c.destroyAllWindows()
