# To use cv2, you must download OpenCV on your python. The terminal code is pip install opencv-python
# This file showcases the video playback feature of our app. Run code to play video, press q to quit and close window
# Note for later: try putting the .bin file in the line 8 and see if it loads out a video
import cv2


def main():
    cap = cv2.VideoCapture("test.mp4")  # This is a league clip from one of my old games from 2018 hehe

    while cap.isOpened():
        ret, frame = cap.read()

        cv2.imshow("video", frame)

        if cv2.waitKey(10) & 0xFFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
