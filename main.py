from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import ScoreBoard

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(n=0)

right_pad = Paddle((350, 0))
left_pad = Paddle((-350, 0))
ball = Ball()
score = ScoreBoard()

screen.listen()
screen.onkey(right_pad.up, "Up")
screen.onkey(left_pad.up, "w")
screen.onkey(right_pad.down, "Down")
screen.onkey(left_pad.down, "s")

while not score.game_over():
    screen.update()
    time.sleep(ball.move_speed)
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.wall_collision()

    elif (ball.distance(right_pad) < 50 and ball.xcor() > 350) or (ball.distance(left_pad) < 50 and ball.xcor() < -350):
        ball.paddle_collision()

    elif ball.xcor() > 350 or ball.xcor() < -350:
        score.update_score(ball.xcor())
        ball.miss()

screen.exitonclick()
