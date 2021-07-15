from turtle import Turtle

MAX_SCORE = 7

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.write_score()

    def write_score(self):
        self.clear()
        self.goto(-100, 200)
        self.write(arg=f"{self.l_score}", font=("Courier", 80, "normal"), align="center")
        self.goto(100, 200)
        self.write(arg=f"{self.r_score}", font=("Courier", 80, "normal"), align="center")

    def update_score(self,xcor):
        if xcor < -340 :
            self.r_score += 1

        else :
            self.l_score += 1

        self.write_score()

    def game_over(self):
        if self.l_score >= 7 or self.r_score >= 7:
            return True

        return False