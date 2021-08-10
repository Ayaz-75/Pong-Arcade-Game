import time
from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

screen = Screen()
screen.setup(800, 600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
b_paddle = Paddle((0, -300))
b_paddle.shapesize(stretch_wid=1, stretch_len=5)

ball_b = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(r_paddle.go_up, "o")
screen.onkey(r_paddle.go_down, "l")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_is_on = True
while game_is_on:
    time.sleep(ball_b.moving_speed)
    screen.update()
    ball_b.move_ball()

    if ball_b.ycor() > 280 or ball_b.ycor() < -280:
        ball_b.bounce_y()

    if ball_b.distance(r_paddle) < 50 and ball_b.xcor() > 320 or ball_b.distance(l_paddle) < 50 and ball_b.xcor() < -320:
        ball_b.bounce_x()

    if ball_b.xcor() > 380:
        ball_b.reset_position()
        scoreboard.refresh_lscore()

    if ball_b.xcor() < -380:
        ball_b.reset_position()
        scoreboard.refresh_rscore()


screen.exitonclick()
