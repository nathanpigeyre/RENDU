import sys
from PyQt5.QtWidgets import *

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        widget = QWidget()
        self.setCentralWidget(widget)
        widget.setWindowTitle("PIGEYRE_Nathan")
        grid = QGridLayout()
        widget.setLayout(grid)
        self.setGeometry(300, 150, 200, 200)
        self.setWindowTitle("PIGEYRE_Nathan")

        Compteur = QLabel("Compteur :")
        self.comp = QLineEdit("0")
        start = QPushButton("Start")
        reset = QPushButton("Reset")
        stop = QPushButton("Stop")
        Connect = QPushButton("Connect")
        quitter = QPushButton("Quitter")

        grid.addWidget(Compteur, 0, 0, 1, 1)
        grid.addWidget(self.comp, 1,0, 1, 2)
        grid.addWidget(start, 2, 0, 1, 2)
        grid.addWidget(reset, 3, 0, 1, 1)
        grid.addWidget(stop, 3, 1, 1, 1)
        grid.addWidget(Connect, 4, 0, 1, 1)
        grid.addWidget(quitter, 4, 1, 1, 1)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())