from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QMessageBox

import FileManagement
import Interface

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


@pyqtSlot()
def import_():
    global current_frames
    if mult:
        files = Interface.openFileNamesDialog()
        FileManagement.files.clear()
        FileManagement.files = files
    else:
        file = Interface.openFileNameDialog()
        FileManagement.files.clear()
        FileManagement.files.append(file)
        current_frames = FileManagement.get_frames()
