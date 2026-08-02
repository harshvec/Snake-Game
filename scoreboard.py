from turtle import Turtle

ALIGNMENT = "center"
FONT = ("courier", 16, "normal")






class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0,260)
        with open("data.txt") as file:
            self.highscore = int(file.read())
        self.score = 0
        self.write(f"Score: {self.score} High Score: {self.highscore}", align=ALIGNMENT, font=FONT)


    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.highscore}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()

    def reset(self):
        if self.highscore < self.score:
            self.highscore = self.score
            with open("data.txt","w") as data:
                data.write(str(self.highscore))
        self.score = 0
        self.update_scoreboard()
