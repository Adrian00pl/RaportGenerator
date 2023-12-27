import sys
from PyQt6.QtWidgets import (
    QMainWindow, QApplication,
    QLabel, QToolBar, QStatusBar,QWidget,QStackedWidget,QHBoxLayout,
)
from PyQt6.QtGui import QAction, QIcon,QActionGroup
from PyQt6.QtCore import Qt, QSize
import FirstWindow,SecondWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle("My App")
        self.setFixedSize(QSize(800, 800))

        first = FirstWindow.FirstWindow()
        second = SecondWindow.SecondWindow()

        self.stack = QStackedWidget(self)
        self.stack.setFixedSize(QSize(800, 800))
        self.stack.addWidget(first)
        self.stack.addWidget(second)

        self.setCentralWidget(self.stack)

        toolbar = QToolBar("My main toolbar")
        toolbar.setMovable(False)
        self.addToolBar(toolbar)
        self.setStatusBar(None)  # Usunięcie paska statusu

        button_action = QAction("Raport RM", self)
        button_action.setStatusTip("This is your button")
        button_action.triggered.connect(lambda: self.onMyToolBarButtonClick(0))
        button_action.setCheckable(True)
        toolbar.addAction(button_action)

        button_action2 = QAction("Second button", self)
        button_action2.setStatusTip("This is your button")
        button_action2.triggered.connect(lambda: self.onMyToolBarButtonClick(1))
        button_action2.setCheckable(True)
        toolbar.addAction(button_action2)

        button_action3 = QAction("Third button", self)
        button_action3.setStatusTip("This is your button")
        button_action3.triggered.connect(lambda: self.onMyToolBarButtonClick(2))
        button_action3.setCheckable(True)
        toolbar.addAction(button_action3)

        toolbargroup = QActionGroup(self)
        toolbargroup.addAction(button_action)
        toolbargroup.addAction(button_action2)
        toolbargroup.addAction(button_action3)

        layout = QHBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)  # Usunięcie marginesów
        layout.addWidget(toolbar)

        widget = QWidget()
        widget.setLayout(layout)
        self.setMenuWidget(widget)

    def onMyToolBarButtonClick(self, i):
        self.stack.setCurrentIndex(i)

def run_app():
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    run_app()
