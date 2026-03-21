from logic import Student_Workspace
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Student_Workspace()
    window.show()
    sys.exit(app.exec_())
