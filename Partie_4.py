import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

class Thread(QThread):
    change = pyqtSignal(int)

    def __init__(self):
        super().__init__()
        self.arret_thread = False

    def run(self):
        counter = 0
        while not self.arret_thread:
            counter += 1
            self.change.emit(counter)
            self.msleep(1000)

    def stop(self):
        self.arret_thread = True
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.thread = Thread()
        self.devoir()

    def devoir(self):
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

        start.clicked.connect(self.__start)
        quitter.clicked.connect(self.quitter)
        reset.clicked.connect(self.reset)
        stop.clicked.connect(self.stop)

        self.thread.change.connect(self.update)

    def __start(self):
        self.thread.arret_thread = False
        self.thread.start()

    def update(self, value):
        self.comp.setText(str(value))

    def stop(self):
        self.thread.stop()
        self.arret_thread = True

    def quitter(self):
        self.thread.arret_thread = True
        QApplication.quit()

    def reset(self):
        self.thread.stop()
        self.comp.setText("0")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
