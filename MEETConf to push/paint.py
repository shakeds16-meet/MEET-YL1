#I have no python3, Sadek coudn't install because laptop has no root access
import turtle
turtle.speed(0)
turtle.penup()
turtle.goto(0,0)
#turtle.pencolor("red")
def draw_circle(x,y):
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()
    turtle.begin_fill()
    turtle.circle(20)
    turtle.end_fill()


#turtle.ondrag()
#turtle.goto(0,0)
#turtle.pendown()
#turtle.circle(10)
#shaked=turtle.Turtle()
#shaked.speed(0)
#shaked.pencolor("blue")
#def draw_b_circle(x,y):
#    turtle.penup()
#    turtle.goto(x,y)
#    turtle.pendown()
#    turtle.circle(20)
#turtle.onscreenclick(draw_b_circle, btn=3)

nadav=turtle.Turtle()
nadav.speed(0)
def pink_pen():	
	turtle.pencolor("pink")
        turtle.color("pink")
def red_pen():
	turtle.pencolor("red")
        turtle.color("red")
def blue_pen():	
	turtle.pencolor("blue")
        turtle.color("blue")
def green_pen():
	turtle.pencolor("green")
        turtle.color("green")

def draw_square(x,y):
	turtle.penup()
	turtle.goto(x,y)
        turtle.begin_fill()
        turtle.pendown()
	turtle.goto(x+20,y)
	turtle.goto(x+20,y+20)
	turtle.goto(x,y+20)
	turtle.goto(x,y)
        turtle.end_fill()

turtle.getscreen().onkey(pink_pen, "p")
turtle.getscreen().onkey(red_pen, "r")
turtle.getscreen().onkey(blue_pen, "b")
turtle.getscreen().onkey(green_pen, "g")


turtle.onscreenclick(draw_square, btn=3)
turtle.onscreenclick(draw_circle)

turtle.getscreen().listen()	
turtle.mainloop()
