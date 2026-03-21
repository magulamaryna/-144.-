import sys
from logic import StarshipApp
from PyQt5.QtWidgets import QApplication


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = StarshipApp()
    window.show()
    sys.exit(app.exec())