from turtle import Screen
import time
from food import Food
from snake import Snake
from scoreboard import ScoreBoard

SPEED = 0.1
s = Screen()
s.setup(width=600, height=600)
s.bgcolor("black")
s.title("Snake Game")
s.tracer(0)
snake = Snake()
food = Food()
score = ScoreBoard()
s.update()
s.listen()
s.onkey(key="Up", fun=snake.up)
s.onkey(key="Down", fun=snake.down)
s.onkey(key="Left", fun=snake.left)
s.onkey(key="Right", fun=snake.right)

game_on = True
while game_on:
    s.update()
    time.sleep(SPEED)
    snake.move()
    if snake.head.distance(food) < 15:
        food.refresh()
        score.refresh()
        snake.extend()
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        score.geme_over()
        game_on = False
    for i in snake.l[1:]:
        if snake.head.distance(i) < 10:
            score.geme_over()
            game_on = False

s.exitonclick()
