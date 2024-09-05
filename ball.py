from turtle import Turtle

class Ball(Turtle):
    x_pos = 0
    y_pos = 0
    x_move = 12
    y_move = 12

    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("square")
        self.color("white")
        self.move_speed = 0.1

    def move(self):
        self.x_pos = self.xcor() + self.x_move
        self.y_pos = self.ycor() + self.y_move
        self.goto(self.x_pos, self.y_pos)

    def bounce(self):
        self.y_move *= -1

    def hit_paddle(self):
        self.x_move *= -1

    def reset_pos(self):
        self.goto(0, 0)
        self.x_move *= -1
        self.move_speed = 0.1

    def increase_speed(self):
        self.move_speed *= 0.9