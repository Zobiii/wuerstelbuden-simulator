from PyQt6.QtWidgets import QApplication
import logging, sys
from utils.logger import setup_logger
from ui.start_screen import StartupScreen


def show_main_menu():
    logging.info("Start-Button gedrückt - Hauptmenü wird geladen")


if __name__ == "__main__":
    setup_logger()
    logging.info("Spiel wird gestartet...")

    app = QApplication(sys.argv)

    start_screen = StartupScreen(start_callback=show_main_menu)
    start_screen.show()

    sys.exit(app.exec())
