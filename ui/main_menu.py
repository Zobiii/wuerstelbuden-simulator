from PyQt6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QLabel,
    QHBoxLayout,
    QPushButton,
    QGridLayout,
)
from PyQt6.QtGui import QPixmap, QIcon
from PyQt6.QtCore import QSize, Qt
import logging, sys
from utils.image_tools import create_rounded_framed_pixmap
from ui.screens.weather_screen import WeatherMenu
from logic.weather_system import WeatherSystem
from ui.screens.storage_screen import StorageScreen
from logic.storage_system import StorageSystem
from ui.screens.supermarket_screen import SupermarketScreen
from logic.supermarket import Supermarket


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.weather_system = WeatherSystem()

        self.supermarket = Supermarket()

        self.storage_system = StorageSystem()
        self.storage_system.add_item("Würstel", 10, 3)
        self.storage_system.add_item("Semmeln", 8, 2)
        self.storage_system.add_item("Senf", 5, 10)

        self.setWindowTitle("Hauptmenü")
        self.setFixedSize(600, 400)

        layout = QVBoxLayout()
        header = QLabel("Was möchtest du tun?")
        header.setAlignment(Qt.AlignmentFlag.AlignCenter)
        header.setStyleSheet("font-size: 20px; font.weigth: bold;")
        layout.addWidget(header)

        # Grid Layout für die vier Ecken
        icon_layout = QGridLayout()
        icon_layout.setSpacing(40)
        icon_layout.setContentsMargins(50, 50, 50, 50)

        # Buttons in den vier Ecken platzieren
        # Oben links
        icon_layout.addWidget(
            self.create_icon_button(
                "Wetter", "resources/icons/wetter.png", self.on_weather
            ),
            0,
            0,
        )
        # Oben rechts
        icon_layout.addWidget(
            self.create_icon_button(
                "Lager", "resources/icons/lager.png", self.on_storage
            ),
            0,
            1,
        )
        # Unten links
        icon_layout.addWidget(
            self.create_icon_button(
                "Supermarkt", "resources/icons/supermarkt.png", self.on_supermarket
            ),
            1,
            0,
        )
        # Unten rechts
        icon_layout.addWidget(
            self.create_icon_button("Bank", "resources/icons/bank.png", self.on_bank),
            1,
            1,
        )

        layout.addLayout(icon_layout)
        self.setLayout(layout)

    def create_icon_button(self, name, image_path, callback):
        btn = QPushButton()
        pixmap = create_rounded_framed_pixmap(
            image_path,
            QSize(120, 120),
            radius=16,
            border_color=Qt.GlobalColor.lightGray,
            border_width=4,
        )
        btn.setIcon(QIcon(pixmap))
        btn.setIconSize(QSize(120, 120))
        btn.setFixedSize(130, 130)
        btn.setToolTip(name)
        btn.clicked.connect(callback)
        return btn

    def on_weather(self):
        logging.info("Wettervorhersage geöffnet")
        self.weather_menu = WeatherMenu(self.weather_system)
        self.weather_menu.show()

    def on_storage(self):
        logging.info("Lager geöffnet")
        self.storage_screen = StorageScreen(self.storage_system)
        self.storage_screen.show()

    def on_supermarket(self):
        logging.info("Supermarkt geöffnet")
        self.supermarket_screen = SupermarketScreen(
            self.supermarket, self.storage_system
        )
        self.supermarket_screen.show()

    def on_bank(self):
        logging.info("Bank geöffnet")
