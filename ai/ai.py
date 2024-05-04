import cv2
import pickledb

db = pickledb.load('../ai/idcam.db', True)

capture = cv2.VideoCapture(db.get('idcam'))
face_cascade = cv2.CascadeClassifier('../cascades/haarcascade_frontalface_default.xml')
eyse_cascade = cv2.CascadeClassifier('../cascades/haarcascade_eye.xml')

while True:
    ret, frame = capture.read()
    faces = face_cascade.detectMultiScale(frame, 1.3, 5)
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
        cv2.putText(frame, 'Face', (x, y), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2, cv2.LINE_AA)
        eyes = eyse_cascade.detectMultiScale(frame, 1.3, 5)
        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(frame, (ex, ey), (ex+ew, ey+eh), (0, 255, 0), 2)
            cv2.putText(frame, 'Eye', (ex, ey), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2, cv2.LINE_AA)
    cv2.imshow('Machine Vision AI', frame)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

capture.release()
cv2.destroyAllWindows()