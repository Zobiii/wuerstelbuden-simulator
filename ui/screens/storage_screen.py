from PyQt6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QLabel,
    QPushButton,
    QHBoxLayout,
    QLineEdit,
)
from PyQt6.QtCore import Qt
from datetime import date
import logging


class StorageScreen(QWidget):
    def __init__(self, storage_system, prices):
        super().__init__()
        self.storage = storage_system
        self.prices = prices
        self.setWindowTitle("Lagerbestand")
        self.setFixedSize(400, 400)
        self.init_ui()

        self.layout = QVBoxLayout()
        self.title = QLabel("Lagerbestand")
        self.title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.title.setStyleSheet("font-size: 18px; font-weight: bold;")
        self.layout.addWidget(self.title)

        self.labels = []

        self.refresh_button = QPushButton("Tageswechsel (Ablauf prüfen)")
        self.refresh_button.clicked.connect(self.advance_day)
        self.layout.addWidget(self.refresh_button)

        self.setLayout(self.layout)
        self.update_display()

    def update_display(self):
        for lbl in self.labels:
            self.layout.removeWidget(lbl)
            lbl.deleteLater()
        self.labels = []

        inv = self.storage.get_inventory()
        for item, entries in inv.items():
            for exp, count in sorted(entries.items()):
                label = QLabel(
                    f"{item}: {count}x gültig bis {exp.strftime('%d.%m.%Y')}"
                )
                self.layout.addWidget(label)
                self.labels.append(label)

    def advance_day(self):
        self.storage.advance_day()
        self.update_display()

    def init_ui(self):
        layout = QVBoxLayout()
        layout.setSpacing(10)

        for item, stack in self.storage.items.items():
            hbox = QHBoxLayout()

            label = QLabel(f"{item} ({len(stack)}x)")
            label.setFixedWidth(150)
            hbox.addWidget(label)

            price_edit = QLineEdit(str(self.prices.get(item, 0.0)))
            price_edit.setFixedWidth(80)
            price_edit.editingFinished.connect(
                lambda i=item, pe=price_edit: self.update_price(i, pe)
            )
            hbox.addWidget(price_edit)

            layout.addLayout(hbox)

        self.setLayout(layout)

    def update_price(self, item, field):
        try:
            new_prices = float(field.text().replace(",", "."))
            self.prices[item] = round(new_prices, 2)
            logging.info(f"Neuer Preis für {item}: {self.prices[item]}€")
        except ValueError:
            logging.info("Ungültiger Preis eingegeben")
