import cv2 as cv

cap = cv.VideoCapture(0)

if not cap.isOpened():
    print("Error in opening the camera")
    exit()

while True:
    ret, frame = cap.read()

    if not ret:
        print("Error in receiving the stream")
        break;

    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    cv.imshow("Frame", gray)

    if cv.waitKey(1) == ord("q"):
        break

cap.release()
cv.destroyAllWindows()


