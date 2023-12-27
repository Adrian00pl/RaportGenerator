import MainWindow
import sys
from PyQt6.QtWidgets import (
    QApplication
)

app = QApplication(sys.argv)
w = MainWindow.MainWindow()
w.show()
app.exec()