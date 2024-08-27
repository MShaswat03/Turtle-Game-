#!/usr/bin/env python
# coding: utf-8

# In[2]:




import turtle
import random

wn = turtle.Screen()
wn.bgpic("Background1.gif")
wn.title("YO!")
wn.setup(width=800, height=600)
wn.tracer(0) 

paddle_a = turtle.Turtle()   
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("red")
paddle_a.penup()
paddle_a.goto(0, 200) 




number_of_asteroids = 5
asteroids = []
for i in range(number_of_asteroids):
    asteroids.append(turtle.Turtle())

for asteroid in asteroids:
    asteroid.shape("circle")
    asteroid.color("green")
    asteroid.penup()
    asteroid.goto(0, -250)  
    asteroid.dy = random.randint(1, 5)/ 4
    x = random.randint(-300, 300)
    asteroid.setposition(x, -250)
    asteroid.shapesize(stretch_wid = random.randint(1, 6))



def paddle_a_right():
    x = paddle_a.xcor()
    x += 20
    paddle_a.setx(x)
   
def paddle_a_left():
    x = paddle_a.xcor()
    x -= 20
    paddle_a.setx(x)
   
wn.listen()
wn.onkeypress(paddle_a_right, "d")
wn.onkeypress(paddle_a_left, "a")

while True:
    wn.update() 
    for asteroid in asteroids:
        y = asteroid.ycor()
        y += asteroid.dy
        asteroid.sety(y)
        if y > 350:
            y = -350
            asteroid.sety(y)
            asteroid.dy = random.randint(1, 5)/ 4
            x = random.randint(-300, 300)
            asteroid.setposition(x, y)
            asteroid.shapesize(stretch_wid = random.randint(1, 6))
  
        


# In[ ]:





# In[ ]:




