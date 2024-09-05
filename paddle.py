from turtle import Turtle

class Paddle(Turtle):

    def __init__(self, x_pos):
        super().__init__()
        self.x_pos = x_pos
        self.new_y = 0
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.shape("square")
        self.color("white")
        self.penup()
        self.goto(self.x_pos, 0)

    def go_up(self):
        self.new_y = self.ycor() + 30
        self.goto(self.x_pos, self.new_y)

    def go_down(self):
        self.new_y = self.ycor() - 30
        self.goto(self.x_pos, self.new_y)


