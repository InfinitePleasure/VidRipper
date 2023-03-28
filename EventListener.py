from PyQt5.QtCore import pyqtSlot

import FileManagement
import output2

all_: bool = False
mult: bool = False
index = 0


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
    print(index)


@pyqtSlot()
def export():
    global all_, index
    FileManagement.extract(all_, index)


@pyqtSlot()
def import_():
    if mult:
        files = output2.openFileNamesDialog()
        FileManagement.files.clear()
        FileManagement.files = files
    else:
        file = output2.openFileNameDialog()
        FileManagement.files.clear()
        FileManagement.files.append(file)
