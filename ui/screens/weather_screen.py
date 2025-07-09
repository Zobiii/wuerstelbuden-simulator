from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton
from PyQt6.QtCore import Qt
from logic.weather_system import WeatherSystem


class WeatherMenu(QWidget):
    def __init__(self, weather_system: WeatherSystem):
        super().__init__()
        self.weather_system = weather_system
        self.setWindowTitle("Wettervorhersage")
        self.setFixedSize(400, 300)

        self.layout = QVBoxLayout()
        self.title = QLabel("7-Tage-Wettervorhersage")
        self.title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.title.setStyleSheet("font-size: 18px; font-weight: bold;")
        self.layout.addWidget(self.title)

        self.forecast_labels = []

        for _ in range(7):
            lbl = QLabel()
            self.forecast_labels.append(lbl)
            self.layout.addWidget(lbl)

        self.refresh_button = QPushButton("Neue Tagesprognose generieren")
        self.refresh_button.clicked.connect(self.advance_day)
        self.layout.addWidget(self.refresh_button)

        self.setLayout(self.layout)
        self.update_forecast()

    def update_forecast(self):
        forecast = self.weather_system.get_forecast()
        for i, day in enumerate(forecast):
            self.forecast_labels[i].setText(
                f"{day['date'].strftime('%a %d.%m')}: {day['weather']}"
            )

    def advance_day(self):
        self.weather_system.advance_day()
        self.update_forecast()
