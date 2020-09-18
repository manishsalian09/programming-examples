import cv2 as cv

cap = cv.VideoCapture(0)

fourcc = cv.VideoWriter_fourcc(*'MJPG')

output = cv.VideoWriter("D:/output.mp4", fourcc, 20.0, (480, 480))


while cap.isOpened():
    ret, frame = cap.read()

    if not ret:
        print("Unable to receive video stream")
        break

    frame = cv.flip(frame, 0)

    output.write(frame)

    cv.imshow("Display", frame)

    if cv.waitKey(1) == ord("q"):
        break

cap.release()
output.release()
cv.destroyAllWindows()
