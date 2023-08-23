import json as j
from logging_config import game_logger
from turtle import Turtle, Screen


ALIGNMENT = "center"
FONT = ("Arial", 20, "bold")


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("White")
        self.penup()
        self.score = 0
        self.current_diff = Level().difficulty()
        self.high_score = self.find_high_score_level(self.current_diff)
        self.goto(0, 280)
        self.update_scoreboard()

    def find_high_score_level(self, diff):
        with open("high_score.txt", "r") as high_score_data:
            high_scores = j.load(high_score_data)
            score = high_scores['high_scores'][diff]
            game_logger.logger.debug("Successfully opened high score file")
        return score

    def update_scoreboard(self):
        """update scoreboard with current score"""
        self.clear()
        game_logger.logger.debug("Cleared Score")
        self.goto(0, 280)
        self.write(arg=f"Level: {self.current_diff.title()}  Score: {self.score}  High Score: {self.high_score}",
                   align=ALIGNMENT, font=FONT)
        game_logger.logger.debug("Displayed new score")

    def reset(self, user_difficulty):
        """resets the score and high score"""

        if self.score > self.high_score:
            self.high_score = self.score
            game_logger.logger.debug("Updating High Score")
            with open("high_score.txt", "r+") as high_score_file:
                high_scores = j.load(high_score_file)
                high_scores['high_scores'][user_difficulty] = self.high_score
                high_score_file.seek(0)
                j.dump(high_scores, high_score_file, sort_keys=True, indent=4)
                game_logger.logger.debug("Updated High Score")
        self.score = 0

        self.update_scoreboard()
        game_logger.logger.debug("Reset score")

    def play_again(self):
        continue_play = Screen().textinput(
            "GAME OVER", "Would you like to continue? (Y/N) ").lower()
        game_logger.logger.debug(f"Continue Play: {continue_play}")
        return continue_play

    def calculate_score(self):
        """adds one to score"""
        self.score += 1
        self.update_scoreboard()
        game_logger.logger.debug(f"Score Updated: {self.score}")

    def end_game(self):
        """renders end game text"""
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)


class Level():
    def __init__(self):
        self.level = ''

    def set_level(self, user_level):
        speed = 0.1
    # set level
        if user_level == 'hard':
            speed = 0.05
        elif user_level == 'medium':
            speed = 0.1
        elif user_level == 'easy':
            speed = 0.2
        else:
            speed
        return speed

    def difficulty(self):
        user_diff = Screen().textinput(
            "Lvl", "What Level would you like to play? (Easy | Medium | Hard) ").lower()

        game_logger.logger.debug(f"User Level: {user_diff}")

        return user_diff
