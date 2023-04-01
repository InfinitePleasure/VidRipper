import errno
import os
import time

import cv2
import numpy as np
from PyQt5.QtWidgets import QMessageBox

files = []


def get_frames() -> np.ndarray:
    if len(files) > 0 and (len(files) > 0 and files[0] != ''):
        for file in files:
            cap = cv2.VideoCapture(file)

            frames = []
            i = 0
            while cap.isOpened():
                ret, frame = cap.read()
                if not ret:
                    break
                frames.append(frame)
                time.sleep(0.01)
                i += 1
            cap.release()
            return frames


def extract(all_, index: int = None):
    if len(files) > 0 and (len(files) > 0 and files[0] != ''):
        for file in files:
            dire = file + "_extract"
            os.makedirs(dire, exist_ok=True)
            cap = cv2.VideoCapture(file)
            i = 0
            while cap.isOpened():
                ret, frame = cap.read()
                if not ret:
                    break
                if not all_ and i == index:
                    cv2.imwrite(str(dire) + "\\" + str(i) + '.jpg', frame)
                    break
                if all_:
                    cv2.imwrite(str(dire) + "\\" + str(i) + '.jpg', frame)
                    time.sleep(0.01)
                i += 1
            cap.release()
    else:
        QMessageBox.critical(None, "Erreur", "Tu dois séléctionner une vidéo")
