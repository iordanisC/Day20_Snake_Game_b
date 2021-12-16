# Day 20, Snake Game, version b OOP

from snake import Snake
from turtle import Screen
import time

game_on = True

screen = Screen()

# screen setup
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake("red", "square", (0,0), 4)

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")

while game_on:
    snake.move_snake()
    screen.update()

    time.sleep(0.2)



screen.exitonclick()