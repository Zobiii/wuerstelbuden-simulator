from PyQt6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QLabel,
    QPushButton,
    QHBoxLayout,
    QSpacerItem,
    QSizePolicy,
)
from PyQt6.QtCore import Qt, QPropertyAnimation, QRect, QEasingCurve, QTimer
from PyQt6.QtGui import QPixmap
import random, logging
import os

from utils.image_tools import create_rounded_framed_pixmap
from ui.screens.day_summary_screen import SummaryScreen


class DayScreen(QWidget):
    def __init__(self, weather, customer_logic, storage, economy, prices):
        super().__init__()

        self.setWindowTitle("Verkaufstag")
        self.setFixedSize(600, 400)

        self.weather = weather
        self.customer_logic = customer_logic
        self.storage = storage
        self.economy = economy
        self.prices = prices

        self.successful_sales = 0
        self.failed_sales = 0
        self.earned = 0.00

        self.customers = self.customer_logic.simulate_day(weather, prices)
        random.shuffle(self.customers)
        self.current_index = -1
        self.selected_item = None

        self.layout = QVBoxLayout()
        self.layout.setSpacing(20)
        self.layout.setContentsMargins(20, 20, 20, 20)
        self.setLayout(self.layout)

        self.customer_label = QLabel(self)
        self.customer_label.setFixedSize(120, 120)
        self.customer_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.customer_label.setStyleSheet("background: transparent;")
        image_container = QVBoxLayout()
        image_container.addSpacerItem(
            QSpacerItem(20, 30, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        )
        image_container.addWidget(
            self.customer_label, alignment=Qt.AlignmentFlag.AlignCenter
        )
        self.layout.addLayout(image_container)

        self.order_label = QLabel("...")
        self.order_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.layout.addWidget(self.order_label)

        self.buttons_layout = QHBoxLayout()
        for item in ["Würstel", "Semmeln", "Senf"]:
            btn = QPushButton(item)
            btn.clicked.connect(lambda checked, i=item: self.select_item(i))
            self.buttons_layout.addWidget(btn)
        self.layout.addLayout(self.buttons_layout)

        self.balance_checkbox = QPushButton("Kontostand live anzeigen")
        self.balance_checkbox.setCheckable(True)
        self.balance_checkbox.toggled.connect(self.toggle_balance_display)
        self.layout.addWidget(
            self.balance_checkbox, alignment=Qt.AlignmentFlag.AlignCenter
        )

        self.balance_label = QLabel(f"Kontostand: {self.economy.get_balance():.2f}€")
        self.balance_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.balance_label.setVisible(False)
        self.layout.addWidget(self.balance_label)

        # Abschicken
        self.send_button = QPushButton("🧾 Abschicken")
        self.send_button.clicked.connect(self.send_order)
        self.layout.addWidget(self.send_button, alignment=Qt.AlignmentFlag.AlignCenter)

        # Start
        self.next_customer()

    def select_item(self, item):
        self.selected_item = item
        self.order_label.setText(f"➡️ Du hast {item} ausgewählt.")

    def send_order(self):
        if not self.selected_item:
            self.order_label.setText("Bitte etwas auswählen.")
            return

        correct_item = self.customers[self.current_index]

        if self.selected_item != correct_item:
            logging.info(
                f"Falscher Artikel geliefert! Gewünscht war: {correct_item}, gegeben: {self.selected_item}"
            )
            self.failed_sales += 1
            self.animate_customer_exit()
            return

        if self.storage.items[self.selected_item]:
            self.storage.items[self.selected_item].pop(0)
            self.economy.earn(self.prices[self.selected_item])
            self.earned += self.prices[self.selected_item]
            logging.info(self.earned)
            self.successful_sales += 1
            self.order_label.setText(f"{self.selected_item} verkauft!")

            if self.balance_checkbox.isChecked():
                self.balance_label.setText(
                    f"Kontostand: {self.economy.get_balance():.2f}€"
                )
        else:
            self.failed_sales += 1
            self.order_label.setText(f"{self.selected_item} ist ausverkauft")

        self.animate_customer_exit()

    def next_customer(self):
        self.selected_item = None
        self.current_index += 1

        if self.current_index >= len(self.customers):
            self.order_label.setText("Tag abgeschlossen!")
            self.customer_label.clear()
            self.show_summary()
            self.send_button.setEnabled(False)
            return

        customer_img = random.choice(os.listdir("resources/customer"))
        path = os.path.join("resources/customer", customer_img)
        pixmap = create_rounded_framed_pixmap(path, self.customer_label.size(), 60)

        QTimer.singleShot(0, lambda: self.prepare_customer(pixmap))

        self.order_label.setText(f"Kunde möchte {self.customers[self.current_index]}")

        # self.animate_customer_enter()

    def animate_customer_enter(self):
        r = random.randint(-200, 200)
        logging.info(f"Enter {r}")
        anim = QPropertyAnimation(self.customer_label, b"geometry")
        anim.setDuration(2000)
        anim.setStartValue(QRect(-150, r, 120, 120))
        anim.setEndValue(QRect(240, 50, 120, 120))
        anim.setEasingCurve(QEasingCurve.Type.OutExpo)
        anim.start()
        self.enter_anim = anim

    def animate_customer_exit(self):
        r = random.randint(-200, 200)
        logging.info(f"Exit {r}")
        anim = QPropertyAnimation(self.customer_label, b"geometry")
        anim.setDuration(2000)
        anim.setStartValue(QRect(240, 50, 120, 120))
        anim.setEndValue(QRect(700, r, 120, 120))
        anim.setEasingCurve(QEasingCurve.Type.InExpo)
        anim.start()
        self.exit_anim = anim

        QTimer.singleShot(2000, self.next_customer)

    def prepare_customer(self, pixmap):
        self.customer_label.hide()
        self.customer_label.setPixmap(pixmap)
        self.customer_label.move(-150, 100)
        self.customer_label.show()
        self.animate_customer_enter()

    def show_summary(self):
        logging.info("wird aufgerufen")
        summary_data = {
            "Kunden heute": len(self.customers),
            "Verkäufe": self.successful_sales,
            "Abgelehnt": self.failed_sales,
            "Einnahmen": f"{self.earned:.2f}€",
        }

        self.summary_screen = SummaryScreen(summary_data)
        self.summary_screen.show()
        logging.info("zeigt an")
        self.close()

    def toggle_balance_display(self):
        self.balance_label.setVisible(True)
