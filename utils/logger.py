import logging


def setup_logger():
    logging.basicConfig(
        level=logging.DEBUG,
        format="%(asctime)s - %(filename)s - %(levelname)s - %(message)s",
        handlers=[logging.FileHandler("wurstelbude.log"), logging.StreamHandler()],
    )
