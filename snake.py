from turtle import Turtle

DISTANCE = 20
RIGHT = 0
UP = 90
LEFT = 180
DOWN = 270
STARTING_POSITIONS = [(0,0),(-20,0),(-40,0)]

class Snake():
    def __init__(self):
        self.l = []
        self.create_snake()
        self.head = self.l[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)


    def add_segment(self, position):
        t = Turtle("square")
        t.color("white")
        t.penup()
        t.shapesize(1, 1, 1)
        t.goto(position)
        self.l.append(t)

    def extend(self):
        self.add_segment(self.l[-1].position())

    def move(self):
        for i in range((len(self.l) - 1), 0, -1):
            self.l[i].goto(self.l[i - 1].pos()[0], self.l[i - 1].pos()[1])
        self.head.fd(DISTANCE)

    def make_turn(self, direction):
        if int(self.head.heading()) != direction:
            self.head.left(direction - int(self.head.heading()))

    def up(self):
        if (int(self.head.heading())) != DOWN:
            self.make_turn(UP)

    def right(self):
        if (int(self.head.heading())) != LEFT:
            self.make_turn(RIGHT)

    def left(self):
        if (int(self.head.heading())) != RIGHT:
            self.make_turn(LEFT)

    def down(self):
        if (int(self.head.heading())) != UP:
            self.make_turn(DOWN)
