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
from logic.economy import Economy
from ui.screens.bank_screen import BankScreen
from logic.customer_logic import CustomerLogic
from ui.screens.day_screen import DayScreen


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.weather_system = WeatherSystem()

        self.supermarket = Supermarket()

        self.economy = Economy()

        self.storage_system = StorageSystem()

        self.customer_logic = CustomerLogic()

        self.prices = {"Würstel": 2.50, "Semmeln": 0.80, "Senf": 0.20}

        self.setWindowTitle("Hauptmenü")
        self.setFixedSize(800, 700)

        layout = QVBoxLayout()
        header = QLabel("Was möchtest du tun?")
        header.setAlignment(Qt.AlignmentFlag.AlignCenter)
        header.setStyleSheet("font-size: 20px; font.weigth: bold;")
        layout.addWidget(header)

        # Grid Layout für die vier Ecken
        icon_layout = QGridLayout()
        icon_layout.setSpacing(60)
        icon_layout.setContentsMargins(60, 30, 60, 30)

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
            2,
        )
        # Unten links
        icon_layout.addWidget(
            self.create_icon_button(
                "Supermarkt", "resources/icons/supermarkt.png", self.on_supermarket
            ),
            2,
            0,
        )
        # Unten rechts
        icon_layout.addWidget(
            self.create_icon_button("Bank", "resources/icons/bank.png", self.on_bank),
            2,
            2,
        )

        # Tag starten Button über die ganze Breite
        icon_layout.addWidget(
            self.create_icon_button(
                "Tag starten", "resources/icons/start.png", self.start_day
            ),
            1,
            1,
        )

        layout.addLayout(icon_layout)
        self.setLayout(layout)

    def create_icon_button(self, name, image_path, callback):
        btn = QPushButton()
        pixmap = create_rounded_framed_pixmap(
            image_path,
            QSize(150, 150),
            radius=16,
            border_color=Qt.GlobalColor.lightGray,
            border_width=4,
        )
        btn.setIcon(QIcon(pixmap))
        btn.setIconSize(QSize(150, 150))
        btn.setFixedSize(160, 160)
        btn.setToolTip(name)
        btn.clicked.connect(callback)
        return btn

    def on_weather(self):
        logging.info("Wettervorhersage geöffnet")
        self.weather_menu = WeatherMenu(self.weather_system)
        self.weather_menu.show()

    def on_storage(self):
        logging.info("Lager geöffnet")
        self.storage_screen = StorageScreen(self.storage_system, self.prices)
        self.storage_screen.show()

    def on_supermarket(self):
        logging.info("Supermarkt geöffnet")
        self.supermarket_screen = SupermarketScreen(
            self.supermarket, self.storage_system, self.economy
        )
        self.supermarket_screen.show()

    def on_bank(self):
        logging.info("Bank geöffnet")
        self.bank_screen = BankScreen(self.economy)
        self.bank_screen.show()

    def start_day(self):
        logging.info("Tagesbeginn wird gestartet...")
        self.day_screen = DayScreen(
            weather=self.weather_system.get_today_weather(),
            customer_logic=self.customer_logic,
            storage=self.storage_system,
            economy=self.economy,
            prices=self.prices,
        )
        self.day_screen.show()
