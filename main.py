from PyQt6.QtWidgets import QApplication
import logging, sys
from utils.logger import setup_logger
from ui.start_screen import StartupScreen
from ui.main_menu import MainWindow
from logic.weather_system import WeatherSystem


def show_main_menu():
    logging.info("Spielstart - Hauptmenü wird angezeigt")
    start_screen.close()

    global main_window
    main_window = MainWindow(weather_system=weather_system)
    main_window.show()


if __name__ == "__main__":
    setup_logger()
    logging.info("Spiel wird gestartet...")

    app = QApplication(sys.argv)

    global start_screen
    start_screen = StartupScreen(start_callback=show_main_menu)

    weather_system = WeatherSystem()

    start_screen.show()

    sys.exit(app.exec())
