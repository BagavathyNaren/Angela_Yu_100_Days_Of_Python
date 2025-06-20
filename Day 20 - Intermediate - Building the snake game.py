from turtle import Screen
from snake import Snake
from food import Food
from snake_scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height= 600)
screen.bgcolor("black")
screen.title("Nokia 3310 Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        scoreboard.reset()
        snake.reset()

    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.reset()
            snake.reset()
      
screen.exitonclick()

# TODO 1 - Create a snake body

# TODO 2 - Move the snake



# TODO 3 - Create snake food.



# TODO 4 - Detect collision with food.



# TODO 5 - Create a scoreboard


# TODO 6 - Detect collision with wall


# TODO 7 - Detect collision with tail.