import sys
import random
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtGui import QPainter, QColor
from PyQt5 import uic, QtCore, QtGui


class Example(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.button.clicked.connect(self.but)
        self.setWindowTitle('Рисование')
        self.show()
        self.flag = False

    def but(self):
        self.flag = True
        self.update()

    def paintEvent(self, event):
        if not self.flag:
            return
        qp = QPainter()
        qp.begin(self)
        self.drawFlag(qp)
        qp.end()


    def drawFlag(self,qp):
        n = random.randint(0, 40)
        for i in range(n):
            a = random.randint(0, 300)
            b = random.randint(0, 300)
            qp.setBrush(QColor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
            qp.drawEllipse(b, b, a, a)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
