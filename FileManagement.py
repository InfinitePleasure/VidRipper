import errno
import os
import time

import cv2
import numpy as np
from PyQt5.QtWidgets import QMessageBox


class FileManagement:
    files = []


def get_frames() -> np.ndarray:
    if len(FileManagement.files) > 0 and (len(FileManagement.files) > 0 and FileManagement.files[0] != ''):
        for file in FileManagement.files:
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


def extract(all_, files, extract_dir, index: int = None):
    if len(files) > 0 and (len(files) > 0 and files[0] != ''):
        for file in files:
            cap = cv2.VideoCapture(file)
            i = 0
            while cap.isOpened():
                ret, frame = cap.read()
                if not ret:
                    break
                if not all_ and i == index:
                    print(file)
                    cv2.imwrite(str(extract_dir) + "/" + str(file).split("/")[-1] + "_" + str(i) + '.jpg', frame)
                    break
                if all_:
                    cv2.imwrite(str(extract_dir) + "/" + str(file).split("/")[-1] + "_" + str(i) + '.jpg', frame)
                    time.sleep(0.01)
                i += 1
            cap.release()
    else:
        QMessageBox.critical(None, "Erreur", "Tu dois séléctionner une vidéo")
