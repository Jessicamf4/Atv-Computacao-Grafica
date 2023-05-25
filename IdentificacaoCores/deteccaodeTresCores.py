import numpy as np
import cv2

from PIL import Image
from IdentificacaoCores.util import get_limits

red = [255, 0, 0]

blue = [255, 0, 0]
green = [0, 255, 0]
colors = [red, green, blue]

cap = cv2.VideoCapture(0)
while True:
    ret, frame = cap.read()

    hsvImage = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    limits = get_limits(colors)

    for i, color in enumerate(colors):
        lowerLimit, upperLimit = limits[i]

        mask = cv2.inRange(hsvImage, lowerLimit, upperLimit)

        mask_ = Image.fromarray(mask)

        bbox = mask_.getbbox()

        if bbox is not None:
            x1, y1, x2, y2 = bbox
            frame = cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 5)

    if color == blue:
        frame = cv2.rectangle(frame, (x1, y1), (x2, y2), (255, 0, 0), 5)
    if color == green:
        frame = cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 255), 5)
    if color == red:
        frame = cv2.rectangle(frame, (x1, y1), (x2, y2), (255, 0, 0), 5)


    cv2.imshow('frame', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()