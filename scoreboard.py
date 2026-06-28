from turtle import Turtle

Y = 260


class ScoreBoard(Turtle):
    def __init__(
        self,
    ):
        super().__init__()
        self.score = 0
        with open("day-20/data.txt",) as data :
           self.high_score = int(data.read())
        self.penup()
        self.color("white")
        self.goto(0, Y)
        self.hideturtle()
        self.sc()

    def sc(self):
        self.clear()
        self.goto(0, Y)
        self.write(
            arg=(f"SCORE_BOARD : {self.score}  HIGH_SCORE {self.high_score}"),
            move="False",
            align="center",
            font=("Arial", 8, "normal"),
        )

   
    def reset(self) :
        if self.score > self.high_score :
            self.high_score = self.score
            with open("day-20/data.txt",mode="w") as data :
                data.write(f"{self.high_score}")
        self.score = 0
        self.sc()

    def up_score(self):
        self.score += 1

        self.sc()
