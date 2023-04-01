from PyQt5.QtWidgets import QApplication, QMainWindow

from Interface import Ui_MainWindow

# Only needed for access to command line arguments
import sys

# You need one (and only one) QApplication instance per application.
# Pass in sys.argv to allow command line arguments for your app.
# If you know you won't use command line arguments QApplication([]) works too.
app = QApplication(sys.argv)

# Create a Qt widget, which will be our window.
Ui = Ui_MainWindow()
window = QMainWindow()
Ui.setupUi(main_window=window)

# Start the event loop.
sys.exit(app.exec_())
