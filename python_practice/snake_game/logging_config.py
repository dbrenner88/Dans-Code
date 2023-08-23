import logging


class GameLogger:
    def __init__(self):
        self.logger = logging.getLogger("snake_game")
        self.logger.setLevel(logging.INFO)

        formatter = logging.Formatter(
            '%(asctime)s - %(levelname)s - %(message)s')

        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.INFO)
        console_handler.setFormatter(formatter)

        self.logger.addHandler(console_handler)


game_logger = GameLogger()
