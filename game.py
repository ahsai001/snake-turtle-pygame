import turtle
import time
import random

# score
score = 0
high_score = 0

delay = 0.1
step = 20

# set up the screen
screen = turtle.Screen()
screen.title("Snake Game")
screen.bgcolor("blue")
screen.setup(width=600, height=600)
screen.tracer(0)


# Snake Head
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("black")
head.penup()
head.goto(0, 100)
head.direction = "stop"

# Snake food
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.shapesize(0.50, 0.50)
food.goto(0, 0)

snake_segments = []


def move():
    if head.direction == "up":
        y = head.ycor()  # y coordinate of the turtle
        head.sety(y + step)

    if head.direction == "down":
        y = head.ycor()  # y coordinate of the turtle
        head.sety(y - step)

    if head.direction == "right":
        x = head.xcor()  # y coordinate of the turtle
        head.setx(x + step)

    if head.direction == "left":
        x = head.xcor()  # y coordinate of the turtle
        head.setx(x - step)


def go_up():
    if head.direction != "down":
        head.direction = "up"


def go_down():
    if head.direction != "up":
        head.direction = "down"


def go_right():
    if head.direction != "left":
        head.direction = "right"


def go_left():
    if head.direction != "right":
        head.direction = "left"


def update_score():
    # update score
    pen.clear()
    pen.write("score: {} High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))


# keyboard bindings
screen.listen()
screen.onkey(go_up, "w")
screen.onkey(go_down, "s")
screen.onkey(go_right, "d")
screen.onkey(go_left, "a")

pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)

update_score()


def reset():
    # Hide the segments
    for segmentX in snake_segments:
        segmentX.goto(1000, 1000)

    # clear segment list
    snake_segments.clear()

    # reset score
    global score
    score = 0

    x = random.randint(-290, 290)
    y = random.randint(-290, 290)
    food.goto(x, y)

    update_score()


# Main game loop
while True:
    screen.update()

    # move the end segment in reverse order
    for index in range(len(snake_segments) - 1, 0, -1):
        x = snake_segments[index - 1].xcor()
        y = snake_segments[index - 1].ycor()
        snake_segments[index].goto(x, y)

    if len(snake_segments) > 0:
        snake_segments[len(snake_segments)-1].showturtle()

    # Move segment 0 to where the head is
    if len(snake_segments) > 0:
        x = head.xcor()
        y = head.ycor()
        snake_segments[0].goto(x, y)

    move()
    time.sleep(delay)

    # check for distance to food
    if head.distance(food) < 15:
        # move the food to a random position on screen
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        food.goto(x, y)

        # add a segment
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("grey")
        new_segment.penup()
        new_segment.hideturtle()
        snake_segments.append(new_segment)

        # Increase the score
        score = score + 10

        if score > high_score:
            high_score = score

        update_score()

    # Check for border collision
    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
        time.sleep(1)
        head.goto(0, 0)
        head.direction = "stop"
        reset()

    # Check for head collision
    for segment in snake_segments[3:]:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0, 0)
            head.direction = "stop"
            reset()







