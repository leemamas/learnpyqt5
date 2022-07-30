import sys
from PyQt5.QtWidgets import QWidget,QApplication,QVBoxLayout,QHBoxLayout,QPushButton,QLineEdit,QTableWidget,QTableWidgetItem,QLabel

class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()

        self.setWindowTitle('my app')

        self.resize(500,500)

        #垂直布局
        layout=QVBoxLayout()

        layout.addLayout(self.init_header())
        layout.addLayout(self.init_middle1())
        layout.addLayout(self.init_middle2())
        layout.addLayout(self.init_footer())

        self.setLayout(layout)

    def init_header(self):
        # 水平布局
        header = QHBoxLayout()
        # 按钮
        btn1 = QPushButton("111")
        btn2 = QPushButton("222")
        btn3 = QPushButton("333")

        header.addWidget(btn1)
        header.addWidget(btn2)
        header.addWidget(btn3)
        header.addStretch()

        return header

    def init_middle1(self):
        middle1 = QHBoxLayout()
        # 输入框
        input = QLineEdit()
        input.setPlaceholderText("input something")
        middle1.addWidget(input)

        return middle1

    def init_middle2(self):
        middle2 = QHBoxLayout()
        table = QTableWidget(3, 4)

        table_header = [
            {"text": "col1", "width": 50},
            {"text": "col2", "width": 120},
            {"text": "col3", "width": 100},
            {"text": "col4", "width": 100},
        ]

        for idx, val in enumerate(table_header):
            item = QTableWidgetItem()
            item.setText(val['text'])
            table.setHorizontalHeaderItem(idx, item)
            table.setColumnWidth(idx, val['width'])

        middle2.addWidget(table)

        return middle2

    def init_footer(self):
        footer = QHBoxLayout()
        # 标签
        label = QLabel("xxxxxxxxx")

        btn4 = QPushButton("cancel")

        footer.addWidget(label)
        footer.addStretch()
        footer.addWidget(btn4)

        return footer

if __name__ == '__main__':
    app=QApplication(sys.argv)
    win=Window()
    win.show()
    sys.exit(app.exec_())