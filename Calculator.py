
# Calculator.py
# Copyright (C) 2024 Leo Hua
# This program is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License 
# as published by the Free Software Foundation; either version 2 of the License, or (at your option) any later version.
# This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty 
# of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.
# You should have received a copy of the GNU General Public License along with this program; 
# if not, see http://www.gnu.org/licenses/.

# 版权 (C) 2024 华利昂
# 本程序是自由软件；您可以按照 GNU 通用公共许可证的条款重新发布和/或修改
# 本程序；可以选择许可证的第 2 版，或（根据您的选择）任何更新的版本。
# 本程序的发布目的是希望它有用，但没有任何担保；甚至没有特定目的下的适销性或
# 适用性的隐含担保。请参阅 GNU 通用公共许可证了解更多详细信息。
# 您应该已经收到一份 GNU 通用公共许可证的副本；如果没有，请参见 <http://www.gnu.org/licenses/>.


import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QPushButton, QGridLayout

class Calculator(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Calculator')

        self.layout = QVBoxLayout()

        self.result_display = QLineEdit()
        self.layout.addWidget(self.result_display)

        self.buttons_layout = QGridLayout()
        buttons = [
            ('7', 0, 0), ('8', 0, 1), ('9', 0, 2), ('/', 0, 3),
            ('4', 1, 0), ('5', 1, 1), ('6', 1, 2), ('*', 1, 3),
            ('1', 2, 0), ('2', 2, 1), ('3', 2, 2), ('-', 2, 3),
            ('0', 3, 0), ('.', 3, 1), ('=', 3, 2), ('+', 3, 3),
        ]

        for text, row, col in buttons:
            button = QPushButton(text)
            button.clicked.connect(self.on_click)
            self.buttons_layout.addWidget(button, row, col)

        self.layout.addLayout(self.buttons_layout)
        self.setLayout(self.layout)

    def on_click(self):
        sender = self.sender()
        text = sender.text()

        if text == '=':
            try:
                result = str(eval(self.result_display.text()))
                self.result_display.setText(result)
            except Exception as e:
                self.result_display.setText('Error')
        else:
            self.result_display.setText(self.result_display.text() + text)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    calc = Calculator()
    calc.show()
    sys.exit(app.exec_())
