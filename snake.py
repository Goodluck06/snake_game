from turtle import Turtle

STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
JUU = 90
CHINI = 270
KULIA = 0
KUSHOTO = 180

class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    # CREATING SNAKE BODY
    def create_snake(self):
        for pos in STARTING_POSITION:
            self.add_snake(pos)

    def add_snake(self, position):
        sqr1 = Turtle('square')
        sqr1.color('white')
        sqr1.penup()
        sqr1.goto(position)
        self.segments.append(sqr1)
    def extend(self):
        self.add_snake(self.segments[-1].position())

    # MOVING A SNAKE
    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            x_cor = self.segments[seg_num - 1].xcor()
            y_cor = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(x_cor, y_cor)
        self.head.forward(20)

    def juu(self):
        if self.head.heading() != CHINI:
            self.head.setheading(JUU)
        # if self.segments[0].heading()==0.0:
        #     self.segments[0].left(90)
        # elif self.segments[0].heading() == 180.0:
        #     self.segments[0].right(90)

    def chini(self):
        if self.head.heading() != JUU:
            self.head.setheading(CHINI)

    def kushoto(self):
        if self.head.heading() != KULIA:
            self.head.setheading(KUSHOTO)

    def kulia(self):
        if self.head.heading() != KUSHOTO:
            self.head.setheading(KULIA)
