import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel,
                             QGridLayout, QPushButton, QVBoxLayout)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont, QFontDatabase

class Calculator(QWidget):
    def __init__(self):
        super().__init__()
        self.screen = QLabel(self)
        self.button_1 = QPushButton("1", self)
        self.button_2 = QPushButton("2", self)
        self.button_3 = QPushButton("3", self)
        self.button_4 = QPushButton("4", self)
        self.button_5 = QPushButton("5", self)
        self.button_6 = QPushButton("6", self)
        self.button_7 = QPushButton("7", self)
        self.button_8 = QPushButton("8", self)
        self.button_9 = QPushButton("9", self)
        self.button_0 = QPushButton("0", self)
        self.button_decimal = QPushButton(".", self)
        self.button_add = QPushButton("+", self)
        self.button_subtract = QPushButton("-", self)
        self.button_multiply = QPushButton("*", self)
        self.button_divide = QPushButton("/", self)
        self.button_square = QPushButton("^2", self)
        self.button_clear = QPushButton("AC", self)
        self.button_C = QPushButton("C", self)
        self.button_equals = QPushButton("=", self)
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Calculator")

        vbox = QVBoxLayout()

        vbox.addWidget(self.screen)

        self.setLayout(vbox)

        self.screen.setAlignment(Qt.AlignCenter)

        grid = QGridLayout()

        grid.addWidget(self.button_1, 2, 0)
        grid.addWidget(self.button_2, 2, 1)
        grid.addWidget(self.button_3, 2, 2)
        grid.addWidget(self.button_4, 1, 0)
        grid.addWidget(self.button_5, 1, 1)
        grid.addWidget(self.button_6, 1, 2)
        grid.addWidget(self.button_7, 0, 0)
        grid.addWidget(self.button_8, 0, 1)
        grid.addWidget(self.button_9, 0, 2)
        grid.addWidget(self.button_0, 3, 0)
        grid.addWidget(self.button_add, 3, 3)
        grid.addWidget(self.button_subtract, 2, 3)
        grid.addWidget(self.button_multiply, 1, 3)
        grid.addWidget(self.button_divide, 0, 3)
        grid.addWidget(self.button_clear, 0, 4)
        grid.addWidget(self.button_equals, 3, 1, 1, 2 )
        grid.addWidget(self.button_decimal, 3, 4)
        grid.addWidget(self.button_C, 1, 4)
        grid.addWidget(self.button_square, 2 ,4)

        vbox.addLayout(grid)

        self.button_1.setObjectName("button1")
        self.button_2.setObjectName("button2")
        self.button_3.setObjectName("button3")
        self.button_4.setObjectName("button_4")
        self.button_5.setObjectName("button_5")
        self.button_6.setObjectName("button_6")
        self.button_7.setObjectName("button_7")
        self.button_8.setObjectName("button_8")
        self.button_9.setObjectName("button_9")
        self.button_0.setObjectName("button_0")
        self.button_add.setObjectName("button_add")
        self.button_subtract.setObjectName("button_subtract")
        self.button_multiply.setObjectName("button_multiply")
        self.button_divide.setObjectName("button_divide")
        self.button_clear.setObjectName("button_clear")
        self.button_equals.setObjectName("button_equals")

        self.setStyleSheet("""
            QWidget{
                background-color: hsl(212, 8%, 20%);       
            }
            QLabel{
                font-size: 50px;
                border: 2px solid;
                background-color: hsl(212, 8%, 60%);
                    
            }
            QPushButton{
                font-size: 20px;  
                background-color: hsl(212, 8%, 39%);
                color: white;             
            }
            QPushButton#button_equals{
                background-color: hsl(25, 83%, 53%);              
            }
            QPushButton#button_clear{
                background-color: #961120;
            }
        """)

        self.button_1.clicked.connect(self.button_1_clicked)
        self.button_2.clicked.connect(self.button_2_clicked)
        self.button_3.clicked.connect(self.button_3_clicked)
        self.button_4.clicked.connect(self.button_4_clicked)
        self.button_5.clicked.connect(self.button_5_clicked)
        self.button_6.clicked.connect(self.button_6_clicked)
        self.button_7.clicked.connect(self.button_7_clicked)
        self.button_8.clicked.connect(self.button_8_clicked)
        self.button_9.clicked.connect(self.button_9_clicked)
        self.button_0.clicked.connect(self.button_0_clicked)
        self.button_add.clicked.connect(self.button_add_clicked)
        self.button_subtract.clicked.connect(self.button_subtract_clicked)
        self.button_multiply.clicked.connect(self.button_multiply_clicked)
        self.button_divide.clicked.connect(self.button_divide_clicked)
        self.button_square.clicked.connect(self.button_square_clicked)
        self.button_decimal.clicked.connect(self.button_decimal_clicked)
        self.button_clear.clicked.connect(self.button_clear_clicked)
        self.button_C.clicked.connect(self.button_C_clicked)
        self.button_equals.clicked.connect(self.calculate)


    def button_1_clicked(self):
        yo = self.screen.text()
        yo += "1"
        self.screen.setText(yo)
    def button_2_clicked(self):
        yo = self.screen.text()
        yo += "2"
        self.screen.setText(yo)
    def button_3_clicked(self):
        yo = self.screen.text()
        yo += "3"
        self.screen.setText(yo)
    def button_4_clicked(self):
        yo = self.screen.text()
        yo += "4"
        self.screen.setText(yo)
    def button_5_clicked(self):
        yo = self.screen.text()
        yo += "5"
        self.screen.setText(yo)
    def button_6_clicked(self):
        yo = self.screen.text()
        yo += "6"
        self.screen.setText(yo)
    def button_7_clicked(self):
        yo = self.screen.text()
        yo += "7"
        self.screen.setText(yo)
    def button_8_clicked(self):
        yo = self.screen.text()
        yo += "8"
        self.screen.setText(yo)
    def button_9_clicked(self):
        yo = self.screen.text()
        yo += "9"
        self.screen.setText(yo)
    def button_0_clicked(self):
        yo = self.screen.text()
        yo += "0"
        self.screen.setText(yo)
    def button_add_clicked(self):
        yo = self.screen.text()
        yo += "+"
        self.screen.setText(yo)
    def button_subtract_clicked(self):
        yo = self.screen.text()
        yo += "-"
        self.screen.setText(yo)
    def button_multiply_clicked(self):
        yo = self.screen.text()
        yo += "*"
        self.screen.setText(yo)
    def button_divide_clicked(self):
        yo = self.screen.text()
        yo += "/"
        self.screen.setText(yo)
    def button_square_clicked(self):
        yo = self.screen.text()
        yo += "**2"
        self.screen.setText(yo)
    def button_decimal_clicked(self):
        yo = self.screen.text()
        yo += "."
        self.screen.setText(yo)
    def button_clear_clicked(self):
        self.screen.clear()
    def button_C_clicked(self):
        yo = self.screen.text()
        x = len(yo)
        yo = yo[0:x-1]
        self.screen.setText(yo)
    def calculate(self):
        try:
            yo = self.screen.text()
            yo = eval(yo)
            yo = f"{yo:.2f}"
            self.screen.setText(yo)
        except ZeroDivisionError:
            print("You can't divide by zero !")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    weather_app = Calculator()
    weather_app.show()
    sys.exit(app.exec_())