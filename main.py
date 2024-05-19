import turtle
import random 
# window.bgpic("space.gif")
# window.addshape("stars.gif")

turtle.title("Space War")
#Create turtle object
t = turtle.Turtle()
t.penup()
#Draw the border
t.goto(-340,320)
t.pensize(3)
t.pendown()
t.forward(670)
t.right(90)
t.forward(620)
t.right(90)
t.forward(670)
t.right(90)
t.forward(620)
t.penup()
t.hideturtle()
#Create a player object
player = turtle.Turtle()
player.shape("classic")
player.color("blue")
player.shapesize(2,2,2)
player.penup()
player.speed(0)
#Create a star object
star = turtle.Turtle()
star.penup()
star .goto(50,0)
star.shape("circle")
star.color("yellow")
star.shapesize(2,2,2)
# star.shape("stars.gif")
star.goto(random.randint(-300,300),random.randint(-300,300))

#Create a scoreboard
scoreboard = turtle.Turtle()
scoreboard.speed(0)
scoreboard.color("red")
scoreboard.penup()
scoreboard.hideturtle()
scoreboard.goto(-300,305)
scoreboard.write("Score: 0", align = "left",font=("arial", 20, "normal"))

#create life board
livesboard = turtle.Turtle()
livesboard.speed(0)
livesboard.color("red")
livesboard.hideturtle()
livesboard.penup()
livesboard.goto(-190,305)
livesboard.write("Lives: 3", align = "left",font=("arial", 20, "normal"))

#Initialise a speed variable
speed = 1
#Initialise score variable
score = 0
#Define alien lists
maurris = []
#lives
lives = 3
#Define turnLeft function,player turn left 30 degrees
def turnLeft():
    player.left(30)
#Define turnRight function, player turns 30 degrees to right
def turnRight():
    player.right(30)
#Define an increase function where player increases speed
def increase():
    global speed
    speed += 1

def isCollision(t1,t2):
    d = ((t1.xcor()-t2.xcor())**2 + (t1.ycor()-t2.ycor())**2)**0.5
    if d < 30:
        return True
    else:
        return False
#Set the keyboard presses
turtle.listen()
#Press left button to turn left
turtle.onkey(turnLeft, "Left")
#Press right button to turn right
turtle.onkey(turnRight, "Right")
#Press up button to increase speed
turtle.onkey(increase, "Up")

#Main Program
startGame = True
while startGame:
    player.forward(speed)
    #Player move forward continously until it touches the border
    if player.pos() == (305.00, 0.00):
        startGame = False

    #Player boundry checking
    if player.xcor() > 300 or player.xcor()<-300 or player.ycor() > 300 or player.ycor() <-300:
        #Touch 180 when touched boundry
        player.left(180)

    #Check for collision
    if isCollision(player,star):
        #Random coordinates for the star to go to
        x = random.randint(-300,300)
        y = random.randint(-300,300)
        star.goto(x,y)
        #Adds the score
        score += 1
        #Update the scoreboard
        scoreboard.clear()
        scoreboard.write("Score: " +str(score) , align = "left",font=("arial", 15, "normal"))
        #Creating maurris and appear randomly
        maurris.append(turtle.Turtle())
        maurris[len(maurris)-1].shape("square")
        maurris[len(maurris)-1].color("red")
        maurris[len(maurris)-1].penup()
        maurris[len(maurris)-1].speed(0)
        maurris[len(maurris)-1].goto(random.randint(-300,300),random.randint(-300,300))
    #Game over when i touch maurris
    for a in maurris:
        if isCollision(player,a):
            lives -= 1
            a.hideturtle()
            maurris.remove(a)
            livesboard.clear()
            livesboard.write("Lives: " + str(lives), align = "left", font=("arial", 20, "normal"))
        if lives == 0:
            startGame = False
##            if score == 1:
##                maurris = turtle.Turtle()
##                maurris.shape("square")
##                maurris.color("red")
##                maurris.penup()
##                maurris.speed()
##                maurris.goto(random.randint(-300 ,300) ,random.randint(-300,300))
##        else:
##           maurris.goto(random.randint(-300 ,300) ,random.randint(-300,300))
##    if score > 0 and isCollision(player,maurris):
##        gameStart = False
#Create a gameover turtle.Turtle()
gameOver = turtle.Turtle()
gameOver.speed(0)
gameOver.color("red")
gameOver.penup()
gameOver.hideturtle()
gameOver.goto(0 , 0)
gameOver.write("GAMEOVER\nScore: " +str(score) , align = "center" , font = ("arial" ,60,"bold"))













