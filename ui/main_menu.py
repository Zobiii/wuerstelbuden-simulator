from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QHBoxLayout, QPushButton
from PyQt6.QtGui import QPixmap, QIcon
from PyQt6.QtCore import QSize, Qt
import logging, sys
from utils.image_tools import create_rounded_framed_pixmap


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Hauptmenü")
        self.setFixedSize(600, 400)

        layout = QVBoxLayout()
        header = QLabel("Was möchtest du tun?")
        header.setAlignment(Qt.AlignmentFlag.AlignCenter)
        header.setStyleSheet("font-size: 20px; font.weigth: bold;")
        layout.addWidget(header)

        icon_layout = QHBoxLayout()
        icon_layout.setSpacing(20)

        icon_layout.addWidget(
            self.create_icon_button(
                "Wetter", "resources/icons/wetter.png", self.on_weather
            )
        )
        icon_layout.addWidget(
            self.create_icon_button(
                "Lager", "resources/icons/lager.png", self.on_storage
            )
        )
        icon_layout.addWidget(
            self.create_icon_button(
                "Supermarkt", "resources/icons/supermarkt.png", self.on_supermarket
            )
        )
        icon_layout.addWidget(
            self.create_icon_button("Bank", "resources/icons/bank.png", self.on_bank)
        )

        layout.addLayout(icon_layout)
        self.setLayout(layout)

    def create_icon_button(self, name, image_path, callback):
        btn = QPushButton()
        pixmap = create_rounded_framed_pixmap(
            image_path,
            QSize(96, 96),
            radius=16,
            border_color=Qt.GlobalColor.lightGray,
            border_width=4,
        )
        btn.setIcon(QIcon(pixmap))
        btn.setIconSize(QSize(96, 96))
        btn.setFixedSize(100, 100)
        btn.setToolTip(name)
        btn.clicked.connect(callback)
        return btn

    def on_weather(self):
        logging.info("Wettervorhersage geöffnet")

    def on_storage(self):
        logging.info("Lager geöffnet")

    def on_supermarket(self):
        logging.info("Supermarkt geöffnet")

    def on_bank(self):
        logging.info("Bank geöffnet")
