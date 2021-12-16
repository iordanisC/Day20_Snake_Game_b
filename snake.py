
#snake class
from turtle import Turtle
import time

segments = []
colors = ("red", "green", "blue", "yellow")
game_on = True

class Snake:

    def __init__(self, color, shape, position, num_of_segments):
        self.create_snake(color, shape, position, num_of_segments)


    def create_snake(self, color, shape, position, num_of_segments):
        pos = position
        for seg in range(num_of_segments):
            new_segment = Turtle()

            new_segment.color(colors[seg])
            new_segment.shape(shape)
            new_segment.setposition(pos)
            segments.append(new_segment)
            pos = new_segment.position()[0] -20, new_segment.position()[1]
        self.head = segments[0]

    def move_snake(self):
        positions = []

        num_of_segments = len(segments)

        for seg in range(num_of_segments):
            positions.append(segments[seg].position())

        self.head.forward(20)

        for seg in range(1, num_of_segments):
            pos = positions[seg -1]
            segments[seg].setposition(pos)


        #print(positions)



    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)
            self.move_snake()

    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)
            self.move_snake()

    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)
            self.move_snake()

    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)
            self.move_snake()

