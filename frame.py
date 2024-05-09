import imutils 
import cv2 

video = ""

result_path = "result_video.avi"

if video == "":
    print("[webcam start]")
    vs = cv2.VideoCapture(0)

else:
    print("[video start]")
    vs = cv2.VideoCapture(video)

writer = None

while True:
    ret, frame = vs.read()

    if frame is None:
        break

    frame = imutils.resize(frame, width=320, height=240)

    cv2.imshow("frame", frame)

    key = cv2.waitKey(1) & 0xFF
    if key == ord("q"):
        break
                                    
    if writer is None:
        fourcc = cv2.VideoWriter_fourcc(*"MJPG")
        writer = cv2.VideoWriter(result_path, fourcc, 25, (frame.shape[1], frame.shape[0]), True)

    if writer is not None:
        writer.write(frame)

vs.release()
cv2.destroyAllWindows()

