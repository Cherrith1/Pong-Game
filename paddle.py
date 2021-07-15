from turtle import Turtle

MOVE = 20

class Paddle(Turtle):
    def __init__(self, position):
        super().__init__(shape="square")
        self.penup()
        self.shapesize(stretch_wid=0.5, stretch_len=5)
        self.color("white")
        self.goto(position)
        self.left(90)

    def up(self):
        if self.ycor() < 280:
            self.forward(MOVE)

    def down(self):
        if self.ycor() > -280:
            self.backward(MOVE)


