from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import ScoreBoard

screen = Screen()
screen.setup(width=600, height=550)
screen.bgcolor("black")
screen.title("SNAKE GAME")
screen.tracer(0)
snake = Snake()
food = Food()
score = ScoreBoard()
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    if snake.HEAD.distance(food) < 15:
        score.up_score()
        food.refresh()
        snake.extend()
    if (
        snake.HEAD.xcor() > 290
        or snake.HEAD.xcor() < -300
        or snake.HEAD.ycor() > 265
        or snake.HEAD.ycor() < -265
    ):
        score.reset()
        snake.remove()
    for tim in snake.turts[1:]:
        if snake.HEAD.distance(tim) < 10:
            score.reset()
            snake.remove()
screen.exitonclick()
