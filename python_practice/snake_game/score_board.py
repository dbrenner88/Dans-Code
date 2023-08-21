from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 20, "bold")


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("White")
        self.penup()
        self.score = 0
        self.goto(0, 280)
        self.update_scoreboard()

    def update_scoreboard(self):
        """update scoreboard with current score"""
        self.write(arg=f"Score Board: {self.score}",
                   align=ALIGNMENT, font=FONT)

    def calculate_score(self):
        """adds one to score"""
        self.score += 1
        self.clear()
        self.update_scoreboard()

    def end_game(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)
