## Gürkan Çetin, 11 June 2017
## GitHub/gurkanctn
##
## inspired from Daniel Shiffman's video, Smart Rockets, on Youtube
##
## TODO:
## done: GROW CIRCLES
## TODO: DO NOT GENERATE A CIRCLE INSIDE ANOTHER CIRCLE!

from tkinter import *
import time, timeit
from random import *
from math import *
from math import sin, cos

WIDTH  = 500
HEIGHT = 500
LifeSpan = 20
Counter = 0

tk = Tk()
canvas = Canvas(tk, width = WIDTH, height = HEIGHT, bg="black")
tk.title("Circle Pack in Python")
img = PhotoImage(file="gurkan.gif")
selfphoto = canvas.create_image(0,0, image=img, state="normal", anchor="nw")
canvas.pack()
tk.update()

##def pixel(x,y):
##    x=math.floor(x)
##    y=math.floor(y)   #math.floor(y)
##    #col=[min((a+b),255) for a,b in zip(list(img.get(x,y)),[10,10,10])]
##    col = (255,255,255)
##    #print(col)
##    col=('#%02X%02X%02X' % (col[0],col[1],col[2]))
##    #print(x,y,col,".")
##    img.put(col,(x,y))

def ellipse(w,x,y,r,col,t):
## draws a circle, centered at x,y, with radius r
## on canvas w
## with color = col; as a col hex code string
## tagged t
    id=w.create_oval(x-r,y-r,x+r,y+r,fill=col,tag=t)

def distance(x1,y1,x2,y2):
    return sqrt((x2-x1)**2+(y2-y1)**2)

class Circle:
    def __init__(self,x,y):
        self.posx = x
        self.posy = y
        col=[min((a+b),255) for a,b in zip(list(img.get(self.posx,self.posy)),[0,0,0])]
        col=('#%02X%02X%02X' % (col[0],col[1],col[2]))
        self.col=col
        self.r = 4
        self.shape = ellipse(canvas,self.posx,self.posy,self.r,self.col,"c")
        self.growable = True
        r = self.r
        
    def grow(self):
        self.r += 1
        self.shape=ellipse(canvas,self.posx,self.posy,self.r,self.col,"c")

    def update(self):
        canvas.move(self.shape, self.xvel, self.yvel)
        self.posx = self.posx + self.xvel
        self.posy = self.posy + self.yvel
        #pos=canvas.coords(self.shape)
        if self.posy > HEIGHT:
            self.posy=1
            self.RocketAlive = False
        if self.posy < 0:
            self.posy = HEIGHT-1
            self.RocketAlive = False
        if self.posx > WIDTH:
            self.posx=1
            self.RocketAlive = False
        if self.posx < 0:
            self.posx = WIDTH-1
            self.RocketAlive = False
        self.xvel += sin(self.DNA[Counter]*2*pi)*0.5
        self.yvel += cos(self.DNA[Counter]*2*pi)*0.5

circles=[]
NumberofCircles = 20
gap=10
for i in range(NumberofCircles):
    x = random()*WIDTH
##    x = i*WIDTH/gap
    x=min(max(floor(x),gap),WIDTH-gap)
    
    y = random()*HEIGHT
##    y = i*HEIGHT/gap
##    y=580
    y=min(max(floor(y),gap),HEIGHT-gap)

    print(x,y)
    circles.append(Circle(x, y))

deadcircles=[]

while True:
##    print("starting...")
##    start = timeit.timeit()
    deadcircles=[]
    for i, circle in enumerate(circles):
        cx=circle.posx
        cy=circle.posy
        cr=circle.r
        if ((cx + cr > WIDTH)  or (cx - cr < 0) or
            (cy + cr > HEIGHT) or (cy - cr < 0)):
            circle.growable = False 
        for j, other in enumerate(circles):
            if j != i:
                if (distance(cx,cy,other.posx,other.posy) <=
                (cr+other.r)):
                    circle.growable = False
                    deadcircles.append(i)
        if circle.growable == True:
            circle.grow()

    ## generate new ones
    for i in deadcircles:
        x = random()*WIDTH
        y = random()*HEIGHT
        x=min(max(floor(x),gap),WIDTH-gap)
        y=min(max(floor(y),gap),HEIGHT-gap)
        circles.append(Circle(x,y))
        
    tk.update()
##    end = timeit.timeit()
##    print (end - start, deadcircles)
tk.mainloop()
