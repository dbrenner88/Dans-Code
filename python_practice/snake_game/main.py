import turtle as t
import time
from snake import Snake
from food import Food
from score_board import ScoreBoard

screen = t.Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)


snake = Snake()
food = Food()
score = ScoreBoard()

level = screen.textinput(
    "Lvl", "What Level would you like to play? (Easy | Medium | Hard) ")
level.lower()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


game_on = True

while game_on:
    speed = 0.1
    # set level
    if level == 'hard':
        speed = 0.05
    elif level == 'medium':
        speed = 0.1
    elif level == 'easy':
        speed = 0.2

    screen.update()
    time.sleep(speed)
    snake.move()
    my_head = snake.head

    # detect collision with food
    if my_head.distance(food) < 15:
        food.refresh()
        score.calculate_score()
        snake.grow_snake()

    if my_head.xcor() > 290 or my_head.xcor() < -290 or my_head.ycor() > 290 or my_head.ycor() < -290:
        game_on = False
        score.end_game()
        print("Game Over")

    for segment in snake.segments[1:]:
        if my_head.distance(segment) < 10:
            game_on = False
            score.end_game()
            print("Game Over")


screen.exitonclick()
