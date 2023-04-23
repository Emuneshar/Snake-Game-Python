import turtle
import time
import random

delay = 0.1

window = turtle.Screen()
window.title("Snake Game")
window.bgcolor("black")
window.setup(width=600, height=600)
window.tracer(0)

# Snake Head
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("white")
head.penup()
head.goto(0,0)
head.direction = "stop"

# Apple (Food)
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("yellow")
food.penup()
food.goto(0,100)

bodySegments = []

# Functions
def goUp():
    head.direction = "up"

def goDown():
    head.direction = "down"

def goLeft():
    head.direction = "left"

def goRight():
    head.direction = "right"

def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y+20)
    
    if head.direction == "down":
        y = head.ycor()
        head.sety(y-20)

    if head.direction == "right":
        x = head.xcor()
        head.setx(x+20)

    if head.direction == "left":
        x = head.xcor()
        head.setx(x-20)

# Keyboard Bindings
window.listen()
window.onkeypress(goUp, "Up")
window.onkeypress(goDown, "Down")
window.onkeypress(goLeft, "Left")
window.onkeypress(goRight, "Right")



# Main game loop

while True:
    window.update()

    # Checking for collisions with food
    # Each basic shape in turtle is 20px by 20px
    if head.distance(food) < 20:
        # Move food to a random spot on the screen
        x = random.randint(-290,290)
        y = random.randint(-290,290)
        food.goto(x, y) 

        # Adding new body segment to the snake
        newSegment = turtle.Turtle()
        newSegment.speed(0)
        newSegment.shape("square")
        newSegment.color("grey")
        bodySegments.append(newSegment)

    # Moving the end segment first
    for i in range(len(bodySegments)-1, 0, -1):
        x = bodySegments[i-1].xcor()
        y = bodySegments[i-1].ycor()
        bodySegments[i].goto(x, y)
    
    # Add code to move the first body segment to where the head is 
    if len(bodySegments) > 0:
        x = head.xcor()
        y = head.ycor()
        bodySegments[0].goto(x, y)
        



    move()

    time.sleep(delay)

window.mainloop()