import turtle
import time

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
head.goto(0,0,)
head.direction = "right"

# Functions
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
        head.sety(y-20)


# Main game loop

while True:
    window.update()

    move()

    time.sleep(delay)

window.mainloop()