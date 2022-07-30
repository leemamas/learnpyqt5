import sys
from PyQt5.QtWidgets import QWidget,QApplication,QVBoxLayout,QHBoxLayout,QPushButton,QLineEdit,QTableWidget,QTableWidgetItem,QLabel

class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()

        self.setWindowTitle('my app')

        self.resize(500,500)

        #垂直布局
        layout=QVBoxLayout()

        #水平布局
        header=QHBoxLayout()
        #按钮
        btn1=QPushButton("111")
        btn2=QPushButton("222")
        btn3=QPushButton("333")

        header.addWidget(btn1)
        header.addWidget(btn2)
        header.addWidget(btn3)
        header.addStretch()

        layout.addLayout(header)
        ##########################################

        middle1=QHBoxLayout()
        #输入框
        input=QLineEdit()
        input.setPlaceholderText("input something")
        middle1.addWidget(input)

        layout.addLayout(middle1)

        ############################################
        middle2=QHBoxLayout()
        #表格,3行4列
        table=QTableWidget(3,4)

        '''
        #列字段
        table_item=QTableWidgetItem()
        table_item.setText("col1")
        table.setHorizontalHeaderItem(0,table_item)
        #列宽度
        table.setColumnWidth(0,50)

        table_item = QTableWidgetItem()
        table_item.setText("col2")
        table.setHorizontalHeaderItem(1, table_item)

        table_item = QTableWidgetItem()
        table_item.setText("col3")
        table.setHorizontalHeaderItem(2, table_item)

        table_item = QTableWidgetItem()
        table_item.setText("col4")
        table.setHorizontalHeaderItem(3, table_item)
        '''

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

        layout.addLayout(middle2)

        #############################


        footer=QHBoxLayout()

        #标签
        label=QLabel("xxxxxxxxx")

        btn4=QPushButton("cancel")

        footer.addWidget(label)
        footer.addStretch()
        footer.addWidget(btn4)

        layout.addLayout(footer)

        # #伸展占位
        # layout.addStretch()
        #窗体设置布局
        self.setLayout(layout)

if __name__ == '__main__':
    app=QApplication(sys.argv)
    win=Window()
    win.show()
    sys.exit(app.exec_())