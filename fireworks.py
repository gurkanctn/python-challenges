## Gürkan Çetin, 9 June 2017
## GitHub/gurkanctn
##
## This python code (3.6.0) uses tkinter library to draw fireworks
## animation on a window.
## Please review, comment and/or improvize.
## Release Notes:
## 1. on explosion, the background is lightened for a cycle
##
## TODO:
## 2. consider adding sound effects with each explosion
## 3. some trails for the ball will be fine (five-pixel long?)
##
## Things I've learned:
## 1. using the Canvas and creating deleting items
## 2. defining functions
## 3. lambda function
## 4. array of objects management (hope my method to kill a ball is correct)
##
## Credits:
## 1) I watched "coding challenge" videos on Youtube: including
##    Fireworks animation, that was coded in Javascript with P5&Processing
##
## 2) the random color string (with lambda function) from Overflow
##
## 3) tkinter framework with bouncing balls, taken from a Youtube tutorial.
##
## ----------------------------------------------------------

from tkinter import *
import time
import random

WIDTH  = 600
HEIGHT = 600

tk= Tk()
canvas = Canvas(tk, width= WIDTH, height= HEIGHT, bg="black")
tk.title("Gurkan")
canvas.pack()

def circle(w, x, y, r,col):
    id = w.create_oval(x-r,y-r,x+r,y+r,fill=col, tag="circle")
    return id

class Particle:
    def __init__(self,x,y):
        self.shape = circle(canvas, x,y,random.random()*2,"white")
        self.xvel=random.random()*3-1.5
        self.yvel=-2+random.random()*2
        self.count=0
        
    def move(self):
        canvas.move(self.shape,self.xvel,self.yvel)
        self.yvel += yacc
        self.count +=1
        
class Ball:
    def __init__(self,size):
        #col=('#%02X%02X%02X' % (r(),r(),r()))
        self.shape = circle(canvas, random.random()*(WIDTH-2*size)*0.5+WIDTH*0.25+size, HEIGHT-size, size,"gray")
        self.xvel = (random.random()*2-1)
        self.yvel = (-10+random.random()*4)
        self.explode=0
        
    def move(self):
        canvas.move(self.shape, self.xvel, self.yvel)
        pos=canvas.coords(self.shape)
        if pos[3] >= HEIGHT or pos[1] <=0:
            canvas.move(self.shape, 0, -self.yvel)
            col=('#%02X%02X%02X' % (r(),r(),r()))
            canvas.itemconfig(self.shape, fill=col)
            self.yvel=-self.yvel  #*0.9
        if pos[2] >= WIDTH or pos[0] <=0:
            canvas.move(self.shape, -self.xvel, 0)
            col=('#%02X%02X%02X' % (r(),r(),r()))
            canvas.itemconfig(self.shape, fill=col)
            self.xvel=-self.xvel  #*0.9
        self.yvel += yacc
        if self.explode==1:
            self.explode=0
        if (self.yvel>=0) and (self.yvel-yacc<0):
            self.explode=1 

yacc=0.125
balls = []
particles = []
r = lambda: random.randint(40,255)
        
for i in range(3):
    balls.append(Ball(random.random()*2+2))

while True:
    ddel = -1
    pdel = -1
    canvas.config(bg="black")
    for i, ball in enumerate(balls):
        ball.move()
        if ball.explode:
            canvas.config(bg="gray")
            posx=(canvas.coords(ball.shape)[0]+canvas.coords(ball.shape)[2])*0.5
            posy=(canvas.coords(ball.shape)[1]+canvas.coords(ball.shape)[3])*0.5
            ddel = i
            for j in range(20):
                particles.append(Particle(posx,posy))
    for i, particle in enumerate(particles):
        particle.move()
        if particle.count>=20:
            pdel = i
    if ddel != -1:
        canvas.delete(balls[ddel].shape)
        del balls[ddel]
        ddel = -1
        balls.append(Ball(random.random()*2+2))
    if pdel != -1:
        canvas.delete(particles[pdel].shape)
        del particles[pdel]
        pdel = -1
    
    
    tk.update()
    time.sleep(0.04)

tk.mainloop()
tk.destroy()
