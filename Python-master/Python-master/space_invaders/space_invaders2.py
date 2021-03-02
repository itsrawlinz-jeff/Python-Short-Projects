import turtle
from turtle import *
import os
import math
import random

# set up the screen
wn = turtle.Screen()
wn.bgcolor("black")
wn.title("Space Invaders")
wn.bgpic("space_invaders_background.gif")

#register shapes
turtle.register_shape("invader.gif")
turtle.register_shape("player.gif")

# Draw border of the game
border_pen = turtle.Turtle()
border_pen.speed(0)
border_pen.color("white")
border_pen.penup()
border_pen.setposition(-300, -300)
border_pen.pendown()
border_pen.pensize(3)
for side in range(4):
    border_pen.fd(600)
    border_pen.lt(90)
border_pen.hideturtle()

#set score to 0
score = 0

#draw the score board
score_pen = turtle.Turtle()
score_pen.speed(0)
score_pen.color("white")
score_pen.penup()
score_pen.setposition(-290, 280)
scorestring = "SCORE: %s" % score
score_pen.write(scorestring, False, align = "left", font = ("Arial", 14, "normal"))
score_pen.hideturtle()


#gameover 
def gameover():
    game_over = turtle.Turtle()
    game_over.speed(0)
    game_over.color("white")
    game_over.setposition(0, 0)
    game_over_string = "GAME OVER %s" % score
    game_over.write(game_over_string, False, align="center", font = ("Arial", 40, "normal"))



# creating our player
player = turtle.Turtle()
player.color("blue")
player.shape("player.gif")
player.penup()
player.speed(0)
player.setposition(0, -250)
player.setheading(90)

# settting our player speed
playerspeed = 15

# chode number of enemies
number_of_enemies = 7


# create an empty list of enemies
enemies = []

enemy = turtle.Turtle()

# add enemies in the list
for i in range(number_of_enemies):
    enemies.append(turtle.Turtle())

x = -200
y = 200
enemy.penup()
for enemy in enemies:
    if enemy.xcor() >= 200:
        enemy.setposition(-200, y - 40)
        enemy.shape("invader.gif")
        enemy.speed('fastest')
        x += 50
    enemy.setposition(x, y)
    enemy.shape("invader.gif")
    enemy.speed(0)
    x += 50
    

# setting our enemey speed
enemyspeed = 2

# create the weapon for our player
bullet = turtle.Turtle()
bullet.color("yellow")
bullet.shape("triangle")
bullet.penup()
bullet.speed('fastest')
bullet.setheading(90)
bullet.shapesize(0.5, 0.5)
bullet.hideturtle()

bulletspeed = 50

# define bullet state
# ready
# fire
bulletstate = "ready"


# define a function that controls the movement
def move_left():
    x = player.xcor()
    x -= playerspeed
    if x < -280:
        x = -280
    player.setx(x)


def move_right():
    x = player.xcor()
    x += playerspeed
    if x > 280:
        x = 280
    player.setx(x)


def fire_bullet():
    # declare bullet as global if it needs to be changed
    global bulletstate
    if bulletstate == "ready":
       # bulletstate = "fire"
        # move the bullet
        bullet.clone()
        x = player.xcor()
        y = player.ycor() + 10
        bullet.setposition(x, y)
        bullet.showturtle()

def isCollision(t1, t2):
    distance = math.sqrt(math.pow(t1.xcor() - t2.xcor(), 2) + math.pow(t1.ycor() - t2.ycor(), 2))
    if distance < 15:
        return True
    else:
        return False

# listen to the keyboard input and use the function defined to use for those keys
turtle.listen()
turtle.onkey(move_left, "Left")
turtle.onkey(move_right, "Right")
turtle.onkey(fire_bullet, "space")


# main game loop
while True:
    for enemy in enemies:
        # move the enemy
        x = enemy.xcor()
        x += enemyspeed
        enemy.setx(x)

        # reverse the enemy when reaches the border
        if enemy.xcor() > 280:
            for e in enemies:
                y = e.ycor()
                y -= 40
                e.sety(y)
            enemyspeed *= -1

        if enemy.xcor() < -280:
            for e in enemies:
                y = e.ycor()
                y -= 40
                e.sety(y)
            enemyspeed *= -1
        if enemy.ycor() > 280:
            for e in enemies:
                e.hideturtle

        # check collision between the bullet and the enemy 
        if isCollision(bullet, enemy):
            # reset bullet
            bullet.hideturtle()
            bulletstate = "ready"
            bullet.setposition(0, -400)
            # hide the enemy
            #enemy.clear()
            enemy.ht()
            #update the score by ten points
            score += 10
            scorestring = "SCORE: %s" % score
            score_pen.clear()
            score_pen.write(scorestring, False, align = "left", font = ("Arial", 14, "normal"))

        if isCollision(player, enemy):
            player.hideturtle()
            enemy.hideturtle()
            gameover()
            break

    # move bullet
    if bulletstate == "ready":
        y = bullet.ycor()
        y += bulletspeed
        bullet.sety(y)
        bullet.speed('fastest')
    
    # check if bullet touches top
    if bullet.ycor() > 275:
        bullet.hideturtle()

