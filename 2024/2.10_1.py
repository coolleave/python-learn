# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '2.10界面.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

import sys
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QWidget, QApplication, QFileDialog


class Ui_Form(QWidget):
    def __init__(self):
        super(Ui_Form, self).__init__()
        self.setupUi(self)
        # 初始化聊天记录
        self.chat_history = []

    def setupUi(self, form):
        form.resize(561, 534)
        self.widget = QtWidgets.QWidget(form)  # 创建对象
        # 设置大小，绘制矩形区域
        self.widget.setGeometry(QtCore.QRect(10, 10, 541, 511))
        # 设置外部容器
        self.container = QtWidgets.QVBoxLayout(self.widget)

        # 调整内容区域与窗口边框之间的间距。
        self.container.setContentsMargins(0, 0, 0, 0)

        # 聊天记录显示
        self.history = QtWidgets.QTextEdit()
        # 设置样式
        self.history.setStyleSheet("background-color: white;\n"
                                   "    color: black;\n"
                                   "    border: 2px solid #4080ff;\n"
                                   "    border-radius: 10px;\n"
                                   "    padding: 10px 20px;\n"
                                   "    font-family: Arial;\n"
                                   "    font-size: 16px;\n"
                                   "    text-align: center;\n"
                                   "    text-decoration: none;\n"
                                   "    qproperty-icon: url(:/images/icon.png);")
        # 设置聊天记录只读读性
        self.history.setReadOnly(True)

        # 添加聊天记录框到外层容器
        self.container.addWidget(self.history)

        # 设置水平容器容纳两个按钮和输入框
        self.h_layout = QtWidgets.QHBoxLayout()

        self.btn_load = QtWidgets.QPushButton(self.widget)
        self.btn_load.setText('上传文件')
        self.btn_load.setStyleSheet("background-color: white;\n"
                                    "    color: black;\n"
                                    "    border: 2px solid #4080ff;\n"
                                    "    border-radius: 10px;\n"
                                    "    padding: 10px 20px;\n"
                                    "    font-family: Arial;\n"
                                    "    font-size: 12px;\n"
                                    "    text-align: center;\n"
                                    "    text-decoration: none;\n"
                                    "    qproperty-icon: url(:/images/icon.png);")

        self.h_layout.addWidget(self.btn_load)

        # 创建输入框
        self.input_box = QtWidgets.QLineEdit(self.widget)
        self.input_box.setPlaceholderText('请输入内容...')
        self.input_box.setStyleSheet("background-color: white;\n"
                                     "    color: black;\n"
                                     "    border: 2px solid #4080ff;\n"
                                     "    border-radius: 10px;\n"
                                     "    padding: 10px 20px;\n"
                                     "    font-family: Arial;\n"
                                     "    font-size: 16px;\n"
                                     "    text-align: center;\n"
                                     "    text-decoration: none;\n"
                                     "    qproperty-icon: url(:/images/icon.png);")

        self.h_layout.addWidget(self.input_box)

        self.btn_send = QtWidgets.QPushButton()
        self.btn_send.setText('发送')
        self.btn_send.setStyleSheet("background-color: white;\n"
                                    "    color: black;\n"
                                    "    border: 2px solid #4080ff;\n"
                                    "    border-radius: 10px;\n"
                                    "    padding: 10px 20px;\n"
                                    "    font-family: Arial;\n"
                                    "    font-size: 12px;\n"
                                    "    text-align: center;\n"
                                    "    text-decoration: none;\n"
                                    "    qproperty-icon: url(:/images/icon.png);")

        # 水平布局器中添加发送按钮
        self.h_layout.addWidget(self.btn_send)
        # 将水平布局器添加到容器中
        self.container.addLayout(self.h_layout)

        # 绑定按钮点击信号和槽函数
        self.btn_load.clicked.connect(self.handle_select_file)
        self.btn_send.clicked.connect(self.handle_send_message)
        self.input_box.returnPressed.connect(self.handle_send_message)

    # 上传文件
    def handle_select_file(self):
        file_dialog = QFileDialog()
        file_path, _ = file_dialog.getOpenFileName(self, "选择文件")
        if file_path:
            pass  # todo

    # 处理发送的信息
    def handle_send_message(self):
        # 赋值输入信息
        message = self.input_box.text()
        # 清除输入信息
        self.input_box.clear()
        # 展示‘我’ 发送的信息
        self.display_message(("我: " + message).rjust(105 - len(message)))  # 设置右对齐
        # 展示 系统回复的信息
        response = self.get_response(message)
        self.display_message("AI: " + response)

    def display_message(self, message):
        # 往聊天记录添加消息
        # self.chat_history.append(message)
        self.history.append(message)

    # 回复聊天信息 todo
    def get_response(self, message):
        return "你好。"


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = Ui_Form()
    w.show()
    app.exec()