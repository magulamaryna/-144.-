from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPixmap
from design import Ui_MainWindow

class Student_Workspace(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.daysList.addItems(['Понеділок', 'Вівторок', 'Середа', 'Четвер', "П'ятниця", 'Субота', 'Неділя'])
        self.ui.addButton.clicked.connect(self.add_task)
        self.ui.daysList.currentRowChanged.connect(self.show_outfit)
    
    def add_task(self):
        task_text = self.ui.taskInput.text()
        if task_text:
            self.ui.tasksList.addItem(task_text)
            self.ui.taskInput.clear()
    
    def show_outfit(self, row):
        image_path = f"dresser/images/{row}.jpg"
        pixmap = QPixmap(image_path)
        
        if not pixmap.isNull():
            self.ui.outfitLabel.setPixmap(pixmap)
            
        else:
            self.ui.outfitLabel.setText("Картинку не знайдено")
