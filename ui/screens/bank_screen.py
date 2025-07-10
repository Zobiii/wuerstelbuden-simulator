from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton
from PyQt6.QtCore import Qt


class BankScreen(QWidget):
    def __init__(self, economy):
        super().__init__()
        self.economy = economy

        self.setWindowTitle("Bank")
        self.setFixedSize(300, 200)

        self.layout = QVBoxLayout()
        self.title = QLabel("🏦 Bank")
        self.title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.title.setStyleSheet("font-size: 18px; font-weight: bold;")
        self.layout.addWidget(self.title)

        self.balance_label = QLabel()
        self.debt_label = QLabel()
        self.layout.addWidget(self.balance_label)
        self.layout.addWidget(self.debt_label)

        self.loan_button = QPushButton("💸 100 € Kredit aufnehmen")
        self.loan_button.clicked.connect(self.take_loan)
        self.layout.addWidget(self.loan_button)

        self.setLayout(self.layout)
        self.update_info()

    def update_info(self):
        self.balance_label.setText(f"💰 Kontostand: {self.economy.get_balance():.2f} €")
        self.debt_label.setText(f"📉 Schulden: {self.economy.get_debt():.2f} €")

    def take_loan(self):
        self.economy.take_loan(100)
        self.update_info()
