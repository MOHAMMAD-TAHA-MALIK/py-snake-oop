from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.turts = []
        self.create_snake()
        self.HEAD = self.turts[0]

    def create_snake(self):
        for tim in STARTING_POSITIONS:
            self.add_seg(tim)

    def add_seg(self, tim):
        new_turtle = Turtle("square")
        new_turtle.color("white")
        new_turtle.penup()
        new_turtle.goto(tim)
        self.turts.append(new_turtle)

    def extend(self):
        self.add_seg(self.turts[-1].position())
    def remove(self):
        for i in self.turts :
            i.goto(1000,1000)
        self.turts.clear()

        self.create_snake()
        self.HEAD = self.turts[0]
    def move(self):
        for t in range(len(self.turts) - 1, 0, -1):
            new_x = self.turts[t - 1].xcor()
            new_y = self.turts[t - 1].ycor()
            self.turts[t].goto(new_x, new_y)
        self.turts[0].forward(MOVE_DISTANCE)

    def up(self):
        if self.HEAD.heading() != DOWN:
            self.HEAD.setheading(90)

    def down(self):
        if self.HEAD.heading() != UP:
            self.HEAD.setheading(270)

    def right(self):
        if self.HEAD.heading() != LEFT:
            self.HEAD.setheading(0)

    def left(self):
        if self.HEAD.heading() != RIGHT:
            self.HEAD.setheading(180)
