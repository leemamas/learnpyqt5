import sys
from PyQt5.QtWidgets import QWidget,QApplication

class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()

        self.setWindowTitle('my app')

        self.resize(500,500)


if __name__ == '__main__':
    app=QApplication(sys.argv)
    win=Window()
    win.show()
    sys.exit(app.exec_())