from turtle import *


#we want to paint a house
#step 1:draw a square

width(7)
color("blue")
forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)
#end of square

#drawing a door

forward(70)
begin_fill()
color("red")
left(90)
forward(120)       
right(90)
forward(60)
right(90)
forward(120)
end_fill()

penup()
goto(200, 200)
pendown()

color("yellow")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()
color("blue")

begin_fill()
left(120)
forward(70)
right(90)
color("cyan")
forward(70)
right(90)
forward(70)
end_fill()
color("blue")
right(90)
forward(70)
right(90)
forward(200)
right(90)
forward(70)
color("cyan")
begin_fill()
right(90)
forward(70)
right(90)
begin_fill()
forward(70)
right(90)
forward(70)
right(90)
forward(70)
end_fill()




exitonclick()