import turtle as t

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake():

    def __init__(self):
        self.segments = []
        self.start_game()
        self.head = self.segments[0]

    def start_game(self):
        """starts the snake game, creating a snake 3 squares long"""

        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        """adds a new """
        snake = t.Turtle(shape="square")
        snake.color("white")
        snake.pu()
        snake.goto(position)
        self.segments.append(snake)

    def move_forward(self, turtle):
        """moves turtle forward 20 px"""
        turtle.forward(20)

    def turn(self, heading, not_heading):
        """turns the turtle based on 2 headings and a number of degrees right and left"""
        first_block = self.head
        my_heading = first_block.heading()
        if my_heading != not_heading:
            first_block.setheading(heading)

    def up(self):
        """turns the turtle up if facing 180 or 0 degree"""
        self.turn(UP, DOWN)

    def down(self):
        """turns the turtle up if facing 180 or 0 degree"""
        self.turn(DOWN, UP)

    def left(self):
        """turns the turtle up if facing 180 or 0 degree"""
        self.turn(LEFT, RIGHT)

    def right(self):
        """turns the turtle up if facing 180 or 0 degree"""
        self.turn(RIGHT, LEFT)

    def move(self):
        """Moves the snake for all sqaures"""
        for seg_num in range(len(self.segments)-1, 0, -1):
            previous_seg = self.segments[seg_num - 1]
            self.segments[seg_num].goto(
                previous_seg.xcor(), previous_seg.ycor())
        self.move_forward(self.head)

    def grow_snake(self):
        """adding a new segment to the snake"""
        pos = self.segments[-1].position()
        self.add_segment(pos)
