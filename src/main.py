from ultralytics import YOLO
import cv2
import math 

cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)

model = YOLO("/home/yolov8n.pt")
classNames = model.names

try:
    while True:
        _, img = cap.read()
        results = model(img, stream=True, verbose=False, conf=0.8)

        for r in results:
            boxes = r.boxes

            for box in boxes:
                x1, y1, x2, y2 = box.xyxy[0]
                x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)

                cv2.rectangle(img, (x1, y1), (x2, y2), (255, 0, 255), 3)

                cls = int(box.cls[0])

                confidence = math.ceil((box.conf[0] * 100)) / 100

                print("name", classNames[cls], "confidence", confidence)

                org = [x1, y1]
                font = cv2.FONT_HERSHEY_SIMPLEX
                fontScale = 1
                color = (255, 0, 0)
                thickness = 2

                cv2.putText(img, classNames[cls], org, font, fontScale, color, thickness)

        cv2.imshow('Camera', img)

        if cv2.waitKey(1) == ord('q'):
            break

except KeyboardInterrupt:
        print("Keyboard Interrupt")

cap.release()
cv2.destroyAllWindows()