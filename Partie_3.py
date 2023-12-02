import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QTimer

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.counter = 0
        self.arret_thread = False
        self.timer = QTimer()
        self.init_ui()

    def init_ui(self):
        widget = QWidget()
        self.setCentralWidget(widget)
        widget.setWindowTitle("PIGEYRE_Nathan")
        grid = QGridLayout()
        widget.setLayout(grid)
        self.setGeometry(300, 150, 200, 200)
        self.setWindowTitle("PIGEYRE_Nathan")

        self.comp = QTextEdit("0")
        start = QPushButton("Start")
        reset = QPushButton("Reset")
        stop = QPushButton("Stop")
        self.connect_button = QPushButton("Connect")
        quitter = QPushButton("Quitter")

        grid.addWidget(QLabel("Compteur :"), 0, 0, 1, 1)
        grid.addWidget(self.comp, 1, 0, 1, 2)
        grid.addWidget(start, 2, 0, 1, 2)
        grid.addWidget(reset, 3, 0, 1, 1)
        grid.addWidget(stop, 3, 1, 1, 1)
        grid.addWidget(self.connect_button, 4, 0, 1, 1)
        grid.addWidget(quitter, 4, 1, 1, 1)

        start.clicked.connect(self.start)
        quitter.clicked.connect(self.quitter)
        reset.clicked.connect(self.reset)
        stop.clicked.connect(self.stop)



    def start(self):
        self.arret_thread = False
        while not self.arret_thread:
            self.counter += 1
            self.comp.setText(str(self.counter))


    def stop(self):
        self.arret_thread = True

    def quitter(self):
        self.arret_thread = True
        QApplication.quit()

    def reset(self):
        self.arret_thread = True
        self.counter = 0
        self.comp.setText("0")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
