import turtle
t = turtle.en()
turtle.bgcolor("black")
colors = ["red", "yellow", "blue", "green"]
 
#ask the user's name using turtle's textinput pop-up window
yourName = turtle.textinput("Enter your name", "What is your name?")
 
#draw a spiral of the name on the screen written 100 times:
for x in range(100):
    t.pencolor(colors[x%4])#rotate through the four colors
    t.penup()#don't draw the regular spiral lines
    t.forward(x*4)#just move the turtle on the screen
    t.pendown()#write the inputted name, bigger each time
    t.write(yourName, font = ("Arial", int( (x + 4) / 4), "bold"))
    t.left(92)#turn left, just as in our other spirals