# To use cv2, you must download OpenCV on your python. The terminal code is: pip install opencv-python
# This file showcases the video playback feature of our app. Run code to play video, press q to quit and close window
# Note for later: try putting the .bin file in the line 8 and see if it loads out a video
import cv2


def playVideo(filename):  # Plays back any video with the same name as the filename

    cap = cv2.VideoCapture(filename)

    while cap.isOpened():
        ret, frame = cap.read()

        if frame is None:
            break

        cv2.imshow(filename[0:-4], frame)

        if cv2.waitKey(10) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
