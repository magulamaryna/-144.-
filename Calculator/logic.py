from PyQt5.QtWidgets import QMainWindow
from design import Ui_MainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.expression = ''

        self.connect_commands()
                
    def connect_commands(self):
        buttons = {
            self.ui.btn_0: {'text': '0'},
            self.ui.btn_1: {'text': '1'},
            self.ui.btn_2: {'text': '2'},
            self.ui.btn_3: {'text': '3'},
            self.ui.btn_4: {'text': '4'},
            self.ui.btn_5: {'text': '5'},
            self.ui.btn_6: {'text': '6'},
            self.ui.btn_7: {'text': '7'},
            self.ui.btn_8: {'text': '8'},
            self.ui.btn_9: {'text': '9'},
            self.ui.btn_plus: {'text': '+'},
            self.ui.btn_minus: {'text': '-'},
            self.ui.btn_multiply: {'text': '*'},
            self.ui.btn_divide: {'text': '/'}
        }
        
        command_btns = {
            self.ui.btn_equal: self.calculate,
            self.ui.btn_backspace: self.backspace,
            self.ui.btn_clear: self.clear
        }
        
        for btn, value in buttons.items():
            btn.clicked.connect(lambda _, symbol=value['text']: self.add_symbol(symbol))
            
        for btn, func in command_btns.items():
            btn.clicked.connect(func)
        
    def add_symbol(self, num):
        self.expression += str(num)
        self.ui.label.setText(self.expression)
        
    def calculate(self):
        if self.expression:
            
            try:
                self.expression = str(round(eval(self.expression), 4))
                self.ui.label.setText(self.expression)
                
            except Exception:
                pass
            
        else:
            pass
    
    def plus_or_minus(self):
        pass
    
    def backspace(self):
        try:
            expr = list(self.expression)
            expr.pop()
            self.expression = ''.join(expr)
            self.ui.label.setText(self.expression)
            
        except Exception:
            pass
    
    def clear(self):
        self.expression = ''
        self.ui.label.setText(self.expression)