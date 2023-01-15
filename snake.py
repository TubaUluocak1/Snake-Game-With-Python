#imports
import turtle
import time
import random

delay = 0.1

#scores
score = 0
high_score = 0

#set up screen
wn = turtle.Screen()
wn.title("Snake Game") 
wn.bgcolor('orange')
wn.setup(width=700 , height=700)
wn.tracer(0)

#snake head
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("black")
head.penup()
head.goto(0,0)
head.direction = "stop"

#snake food
food =turtle.Turtle()
food.speed(0)
food.shape("square")
food.color("red")
food.penup()
food.goto(0,100)

segments = []

#scoreboards
sc = turtle.Turtle()
sc.speed(0)
sc.shape("square")
sc.color("black")
sc.penup()
sc.hideturtle()
sc.goto(0,310)
sc.write("Score: 0 High Score: 0",align="center",font=("Courier", 24, "normal"))

#functions
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

#keyboards bindings
wn.listen()
wn.onkeypress(go_up,"w")
wn.onkeypress(go_down,"s")
wn.onkeypress(go_right,"d")
wn.onkeypress(go_left,"a")

wn.onkeypress(go_up,"Up")
wn.onkeypress(go_down,"Down")
wn.onkeypress(go_right,"Right")
wn.onkeypress(go_left,"Left")

#MainLoop
while True:
    wn.update()

    #check collision with border area
    if head.ycor()<-330 or head.ycor()>330 or head.xcor()<-330 or head.xcor()>330: 
        time.sleep(1)
        head.goto(0,0)
        head.direction = "stop"

        #hide the segments of body
        for segment in segments:
            segment.goto(2000,2000) #out of range
        #clear the segments
        segments.clear()

        #reset score
        score = 0

        #reset delay
        delay = 0.1

        sc.clear()
        sc.write("Score: {} High Score: {}".format(score,high_score),align="center", font=("Courier", 24, "normal"))

    #check collision with food
    if head.distance(food) <20:
        #move the food to random place
        x = random.randint(-310,310)
        y = random.randint(-310,310)
        food.goto(x,y)

        #add a new segment to the head
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("black")
        new_segment.penup()
        segments.append(new_segment)

        #shorten the delay
        delay -= 0.001
        #increase the score
        score += 10

        if score > high_score:
            high_score = score
        sc.clear()
        sc.write("Score: {} High Score: {}".format(score,high_score),align="center",font=("Courier", 24, "normal"))
        
    #move the sehments in reverse order
    for index in range(len(segments)-1,0,-1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x,y)
    #move segment 0 to head
    if len(segments)>0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x,y)

    move()

    #check for collision with body
    for segment in segments:
        if segment.distance(head)<20:
            time.sleep(1)
            head.goto(0,0)
            head.direction = "stop"

            #hide segments
            for segment in segments:
                segment.goto(2000,2000)
            segments.clear()
            score = 0
            delay = 0.1

            #update the score
            sc.clear()
            sc.write("Score: {} High Score: {}".format(score,high_score),align="center",font=("Courier",24,"normal"))

    time.sleep(delay)
wn.mainloop()
