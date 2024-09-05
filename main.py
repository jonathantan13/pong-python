from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)

scoreboard = Scoreboard()

game_on = True
player_1_score = 0
player_2_score = 0

player_1 = Paddle(350)
player_2 = Paddle(-350)
ball = Ball()

screen.listen()
screen.onkey(player_1.go_up, "Up")
screen.onkey(player_1.go_down, "Down")
screen.onkey(player_2.go_up, "w")
screen.onkey(player_2.go_down, "s")

while game_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()

    if ball.distance(player_1) < 50 and ball.xcor() > 320 or ball.distance(player_2) < 50 and ball.xcor() < -320:
        ball.hit_paddle()
        ball.increase_speed()

    if ball.xcor() > 400:
        scoreboard.p2_point()
        ball.reset_pos()
    if ball.xcor() < -400:
        scoreboard.p1_point()
        ball.reset_pos()

screen.exitonclick()