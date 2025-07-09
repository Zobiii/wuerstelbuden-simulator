from PyQt6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QLabel,
    QPushButton,
    QHBoxLayout,
    QSpinBox,
)
from PyQt6.QtCore import Qt


class SupermarketScreen(QWidget):
    def __init__(self, supermarket, storage_system):
        super().__init__()
        self.supermarket = supermarket
        self.storage = storage_system

        self.setWindowTitle("Supermarkt")
        self.setFixedSize(400, 300)

        self.layout = QVBoxLayout()
        self.title = QLabel("Heutige Angebote")
        self.title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.title.setStyleSheet("font-size: 18px; font-weight: bold;")
        self.layout.addWidget(self.title)

        self.spinboxes = {}
        self.price_labels = {}

        self.prices = self.supermarket.get_prices()

        for item, price in self.prices.items():
            row = QHBoxLayout()

            label = QLabel(f"{item}: {price:.2f} €")
            self.price_labels[item] = label
            row.addWidget(label)

            spin = QSpinBox()
            spin.setRange(0, 100)
            self.spinboxes[item] = spin
            row.addWidget(spin)

            self.layout.addLayout(row)

        self.buy_button = QPushButton("Kaufen")
        self.buy_button.clicked.connect(self.buy_items)
        self.layout.addWidget(self.buy_button)

        self.setLayout(self.layout)

    def buy_items(self):
        for item, spinbox in self.spinboxes.items():
            qty = spinbox.value()
            if qty > 0:
                # einfache Haltbarkeitslogik
                if item == "Würstel":
                    self.storage.add_item(item, qty, 3)
                elif item == "Semmeln":
                    self.storage.add_item(item, qty, 2)
                elif item == "Senf":
                    self.storage.add_item(item, qty, 10)
                spinbox.setValue(0)
