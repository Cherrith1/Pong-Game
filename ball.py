from turtle import Turtle

MOVE = 10


class Ball(Turtle):
    def __init__(self):
        super().__init__(shape="circle")
        self.color("white")
        self.penup()
        self.setheading(45)
        self.move_speed = 0.1

    def move(self):
        self.forward(MOVE)

    def wall_collision(self):
        self.setheading(-1 * self.heading())

    def paddle_collision(self):
        self.move_speed *= 0.8
        if self.heading() > 0:
            self.setheading(180 - self.heading())

        else:
            self.setheading(self.heading() - 180)

    def miss(self):

        if self.xcor() < -340:
            angle = 45
        else:
            angle = 135

        self.goto(0,0)
        self.setheading(angle)
        self.move_speed = 0.1
