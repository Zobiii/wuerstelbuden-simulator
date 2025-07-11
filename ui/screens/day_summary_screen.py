from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton
from PyQt6.QtCore import Qt


class SummaryScreen(QWidget):
    def __init__(self, summary_data: dict):
        super().__init__()
        self.setWindowTitle("Tagesauswertung")
        self.setFixedSize(400, 300)

        layout = QVBoxLayout()
        layout.setSpacing(10)

        title = QLabel("Tagesbericht")
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title.setStyleSheet("font-size: 18px; font-weight: bold;")
        layout.addWidget(title)

        for key, value in summary_data.items():
            label = QLabel(f"{key}: {value}")
            label.setAlignment(Qt.AlignmentFlag.AlignLeft)
            layout.addWidget(label)

        close_btn = QPushButton("OK")
        close_btn.clicked.connect(self.close)
        layout.addWidget(close_btn, alignment=Qt.AlignmentFlag.AlignCenter)

        self.setLayout(layout)
