from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QMessageBox

import FileManagement

all_: bool = False
mult: bool = False
index = 0
current_frames = []


@pyqtSlot()
def all_func():
    global all_
    all_ = not all_


@pyqtSlot()
def mult_func():
    global mult
    mult = not mult


@pyqtSlot()
def setIndex(index_):
    global index
    index = index_


@pyqtSlot()
def export():
    global all_, index
    FileManagement.extract(all_, index)
    QMessageBox.about(None, "Extraction", "Extraction terminée !")

