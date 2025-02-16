from turtle import Turtle
STARTING_POSITION = [(0,0), (-20,0), (-40,0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
class Snake(Turtle):
    def __init__(self):
        super().__init__()
        self.all_turtles = []
        self.create_snake()
        self.head = self.all_turtles[0]

    def create_snake(self):
        for position in STARTING_POSITION:
            self.add_turtle(position)

    def add_turtle(self, position):
        new_turtle = Turtle("square")
        new_turtle.color("white")
        new_turtle.penup()
        new_turtle.setpos(position)
        self.all_turtles.append(new_turtle)

    def extend(self):
        self.add_turtle(self.all_turtles[-1].position())

    def reset(self):
        for turtle in self.all_turtles:
            turtle.goto(1000, 1000)
        self.all_turtles.clear()
        self.create_snake()
        self.head = self.all_turtles[0]

    def move(self):
        for tim in range(len(self.all_turtles) - 1, 0, -1):
            new_x = self.all_turtles[tim - 1].xcor()
            new_y = self.all_turtles[tim - 1].ycor()
            self.all_turtles[tim].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
