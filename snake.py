from turtle import Turtle


STARTING_COORDINATE = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP=90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
        self.segments = []
        self.generate_snake()
        self.head = self.segments[0]

    def generate_snake(self):
        for position in STARTING_COORDINATE:
            self.add_segment(position)

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)

        self.segments[0].forward(MOVE_DISTANCE)

    def up_key(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down_key(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left_key(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right_key(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def add_segment(self,position):
        square = Turtle(shape="square")
        square.goto(position)
        square.color("white")
        square.penup()
        self.segments.append(square)

    def extend_snake(self):
        self.add_segment(self.segments[-1].position())

    def reset(self):
        for seg in self.segments:
            seg.goto(1000,1000)
        self.segments.clear()
        self.generate_snake()
        self.head = self.segments[0]