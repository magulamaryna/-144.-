import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from design import Ui_MainWindow

class StarshipApp(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.dial_speed.valueChanged.connect(self.check_engine)
        self.btn_jump.clicked.connect(self.perform_jump)

    def check_engine(self, speed):
        if speed == 0:
            self.label_status.setText("🛰 Корабель у дрейфі...")
            
        elif 1 <= speed < 90:
            self.label_status.setText(f"🚀 Політ нормальний. Швидкість: {speed} св.р.")
            self.label_status.setStyleSheet("color: #94a3b8; background-color: #1e293b;")
            
        else:
            self.label_status.setText("⚠ УВАГА! НЕБЕЗПЕКА! ДВИГУН ПЕРЕГРІТИЙ!")
            self.label_status.setStyleSheet("color: white; background-color: #991b1b;")

    def perform_jump(self):
        current_speed = self.dial_speed.value()
        
        if current_speed > 80:
            self.label_status.setText("✨ ГІПЕРСТРИБОК ВИКОНАНО! ✨")
            self.dial_speed.setValue(0)
            
        else:
            self.label_status.setText("❌ Недостатньо швидкості для стрибка!")


