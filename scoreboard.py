from turtle import Turtle, Screen
screen = Screen()
screen.tracer(0)
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as file:
            self.high_score = file.read()
    def title(self):
        self.setpos(x=0, y=260)
        self.color("white")
        self.update_scoreboard()
        self.hideturtle()

    def update_scoreboard(self):
        self.clear()
        self.write(arg=f"score: {self.score} High score: {self.high_score}", move=False, align="center", font=('Arial', 24, 'normal'))

    def increase_score(self):
        self.score +=1
        self.update_scoreboard()

    def reset(self):
        if self.score > int(self.high_score):
            with open("data.txt", mode="w") as file:
                self.high_score = file.write(str(self.score))
            self.high_score = self.score
        self.score = 0
        self.update_scoreboard()
