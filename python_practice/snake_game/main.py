from food import Food
from score_board import ScoreBoard, Level
from snake import Snake
from logging_config import game_logger
import time
import turtle as t

screen = t.Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)


snake = Snake()
food = Food()
score = ScoreBoard()


def reset_game_ask():
    game_logger.logger.debug("Waiting for user input")
    again = score.play_again()
    game_logger.logger.info("crashed")
    if again == 'y':
        resetting_game()
    else:
        ending_game()


def resetting_game():
    game_logger.logger.debug("User chose to play again")
    score.reset(score.current_diff)
    snake.reset()
    player_level = Level().difficulty()
    score.current_diff = player_level
    speed = Level().set_level(player_level)
    score.update_scoreboard()
    food.refresh()
    game_logger.logger.info(f"current level - {score.current_diff}")
    game_logger.logger.info("playing again")


def ending_game():
    global game_on
    game_on = False
    game_logger.logger.debug("User chose to quit")
    score.end_game()
    game_logger.logger.info("Quit and ended game")


game_on = True


while game_on:

    # game_logger.logger.debug("Updating screen")

    screen.listen()
    screen.onkey(snake.up, "Up")
    screen.onkey(snake.down, "Down")
    screen.onkey(snake.left, "Left")
    screen.onkey(snake.right, "Right")

    level = Level()
    speed = level.set_level(score.current_diff)

   # game_logger.logger.debug(speed)

    screen.update()
    time.sleep(speed)
    snake.move()
    my_head = snake.head

    # game_logger.logger.debug(f"My head position: {my_head.position()}")

    # detect collision with food
    if my_head.distance(food) < 15:
        game_logger.logger.info("got food")
        food.refresh()
        game_logger.logger.debug(f"Shape {food.shape()}")
        game_logger.logger.debug(f"score: {score.score}")
        score.calculate_score()
        snake.grow_snake()

    # detect collision with wall
    if my_head.xcor() > 290 or my_head.xcor() < -290 or my_head.ycor() > 290 or my_head.ycor() < -290:
        reset_game_ask()

    # detect collision with self
    for segment in snake.segments[1:]:
        if my_head.distance(segment) < 10:
            reset_game_ask()


screen.exitonclick()
