import sys

from random import randint

from PyQt5.QtGui import QPainter, QColor, QPen
from PyQt5.QtWidgets import QApplication, QMainWindow

from UI import Ui_MainWindow


class Window(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()

        self.now_circles = None  # список из кортежей (цвет, радиус, координаты)

        self.setupUi(self)
        
        self.setWindowTitle('Git и случайные окружности')

        self.setMinimumSize(550, 550)

        self.btn.clicked.connect(self.func)

    def paintEvent(self, event):
        if self.now_circles:
            qp = QPainter()
            qp.begin(self)
            self.draw_circles(qp)
            qp.end()

    def draw_circles(self, qp):
        for color, r, x, y in self.now_circles:
            qp.setPen(QPen(color, 7))
            qp.drawEllipse(x, y, r, r)

    def func(self):
        kol = self.spinBox.value()
        self.now_circles = [(QColor(randint(0, 255), randint(0, 255),
                                    randint(0, 255)), r := randint(10, 400),
                             randint(10, self.width() - r),
                             randint(10, self.height() - r)) for _ in range(kol)]
        self.repaint()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    wind = Window()
    wind.show()
    sys.exit(app.exec())
