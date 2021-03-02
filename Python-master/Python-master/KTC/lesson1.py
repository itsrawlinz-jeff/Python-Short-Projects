#import the python turtle library 
import turtle

#create the window for our project
wn = turtle.Screen()

#set the color of our background for the window to black
wn.bgcolor("black")

#give the title of our window to "Kids That Code"
wn.title("Kids That Code")

#create our pen and store into variable 't'
t = turtle.Pen()

#list of colors we will be using
colors = ['red', 'purple', 'blue', 'green', 'orange', 'yellow']

#for loop to draw a spiral 360 times
for x in range(360):
    #rotate through the six colors
    t.pencolor(colors[x%6])
    #
    t.width(x/100+1)
    #move the turtle forward 
    t.forward(x)
    #move turtle to the left
    t.left(59)