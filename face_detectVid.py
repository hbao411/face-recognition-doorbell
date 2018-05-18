# using code fomr https://realpython.com/face-detection-in-python-using-a-webcam/
import cv2
import sys
def faceDetect(cascade):
    cap = cv2.VideoCapture(0)

    # Define the codec and create VideoWriter object
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter('output.avi',fourcc, 20.0, (640,480))
    confirmedFace = 0
    numPhotos = 0
    while(cap.isOpened()):
        ret, frame = cap.read()
        if ret==True:
            cascPath = cascade

            # Create the haar cascade
            faceCascade = cv2.CascadeClassifier(cascPath)

            # Read the image
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            # Detect faces in the image
            faces = faceCascade.detectMultiScale(
                gray,
                scaleFactor=1.1,
                minNeighbors=5,
                minSize=(30, 30)
                #flags = cv2.CV_HAAR_SCALE_IMAGE
            )
            if (len(faces) > 0):
                confirmedFace += 1

            print("Found {0} faces!".format(len(faces)))

            # Draw a rectangle around the faces
            for (x, y, w, h) in faces:
                cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
            cv2.imshow("Faces found", frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
            if cv2.waitKey(1) & 0xFF == ord('p'):
                cv2.imwrite("face" + str(numPhotos) + ".png", frame)
        else:
            break

    # Release everything if job is finished
    cap.release()
    out.release()
    cv2.destroyAllWindows()