from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton
from PyQt6.QtCore import Qt
from datetime import date


class StorageScreen(QWidget):
    def __init__(self, storage_system):
        super().__init__()
        self.storage = storage_system
        self.setWindowTitle("Lagerbestand")
        self.setFixedSize(400, 400)

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
