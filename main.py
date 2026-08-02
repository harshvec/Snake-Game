from turtle import Turtle,Screen
from snake import  Snake
import time
from food import Food
from scoreboard import Score

my_screen = Screen()
my_screen.setup(width=600,height=600)
my_screen.bgcolor("black")
my_screen.title("My snake game")
my_screen.tracer(0)

snake = Snake()
food = Food()



my_screen.listen()
my_screen.onkey(snake.up_key,key="Up")
my_screen.onkey(snake.down_key, "Down")
my_screen.onkey(snake.left_key,"Left")
my_screen.onkey(snake.right_key,"Right")

scoreboard = Score()

game_is_on = True
while game_is_on:
    my_screen.update()
    time.sleep(0.1)

    snake.move()

    #detect collision with food
    if food.distance(snake.head) < 15:
        food.refresh()
        snake.extend_snake()
        scoreboard.increase_score()


    #detect collision with wall
    if snake.head.xcor()>280 or snake.head.xcor()<-280 or snake.head.ycor()>280 or snake.head.ycor()<-280:
        scoreboard.reset()
        snake.reset()

    #detect collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.reset()
            snake.reset()





# Move turtle to (0, 0) (not write!)
scoreboard.goto(0, 0)


my_screen.exitonclick()









