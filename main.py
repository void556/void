import sys
from PySide6.QtWidgets import QApplication, QLabel, QVBoxLayout, QWidget


class VoidApp(QWidget):

  def __init__(self):
    super().__init__()
    self.setWindowTitle("Quantum Void Pro")
    self.setStyleSheet("background-color: black;")

    layout = QVBoxLayout()
    self.label = QLabel(
        "This app does absolutely nothing.\nIf you hate me, email me at"
        " saifanayyat18@gmail.com",
        self,
    )
    self.label.setStyleSheet("color: white; font-size: 16px;")
    self.label.setWordWrap(True)

    layout.addWidget(self.label)
    self.setLayout(layout)
    self.showMaximized()


if __name__ == "__main__":
  app = QApplication(sys.argv)
  ex = VoidApp()
  sys.exit(app.exec())
