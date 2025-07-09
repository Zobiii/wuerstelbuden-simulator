from PyQt6.QtWidgets import QWidget, QVBoxLayout, QPushButton, QLabel
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import Qt


class StartupScreen(QWidget):
    def __init__(self, start_callback):
        super().__init__()
        self.setWindowTitle("Würstelbuden-Simulator")
        layout = QVBoxLayout()

        logo = QLabel()
        logo.setPixmap(
            QPixmap("resources/logo.png").scaledToWidth(
                300, Qt.TransformationMode.SmoothTransformation
            )
        )
        logo.setAlignment(Qt.AlignmentFlag.AlignCenter)

        start_button = QPushButton("Spiel starten")
        start_button.clicked.connect(start_callback)

        layout.addWidget(logo)
        layout.addWidget(start_button)
        self.setLayout(layout)
