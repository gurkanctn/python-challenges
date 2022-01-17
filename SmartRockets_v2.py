## Gürkan Çetin, 11 June 2017
## GitHub/gurkanctn
##
## inspired from Daniel Shiffman's video, Smart Rockets, on Youtube
##
## TODO:
## start

from tkinter import *
import time, timeit
from random import *
from math import *
from math import sin, cos

WIDTH  = 400
HEIGHT = 200
LifeSpan = 20
Counter = 0

maxFitness = 0

tk = Tk()
canvas = Canvas(tk, width = WIDTH, height = HEIGHT, bg="black")
tk.title("Smart Rockets in Python")
canvas.pack()

img = PhotoImage(width=WIDTH, height=HEIGHT)
canvas.create_image((WIDTH*0.5, HEIGHT*0.5), image=img, state="normal")

def pixel(x,y):
    x=int(x)
    y=int(y)   #math.floor(y)
    #col=[min((a+b),255) for a,b in zip(list(img.get(x,y)),[10,10,10])]
    col = (255,255,255)
    #print(col)
    col=('#%02X%02X%02X' % (col[0],col[1],col[2]))
    #print(x,y,col,".")
    img.put(col,(x,y))

def circle(w,x,y,r,col,t):
## draws a circle, centered at x,y, with radius r
## on canvas w
## with color = col; as a col hex code string
## tagged t
    id=w.create_oval(x-r,y-r,x+r,y+r,fill=col,tag=t)
    return id

def distance(x1,y1,x2,y2):
    return sqrt((x2-x1)**2+(y2-y1)**2)

class Target:
    def __init__(self,x,y):
        self.posx = x
        self.posy = y
        self.shape = circle(canvas, x, y, 4,"red","Target")
        
class Rocket:
    def __init__(self,x,y):
        self.posx = floor(WIDTH/2)
        self.posy = HEIGHT-20
        self.shape=circle(canvas,self.posx,self.posy,4,"white","c")
        #rocket(self.posx,self.posy)  # pixel is faster than self.shape
        self.xvel = 0
        self.yvel = -2
        self.DNA=[]
        for i in range(LifeSpan):
            self.DNA.append(random())
##        print(self.DNA)
        self.RocketAlive = True
        

    def calcFitness(self):
        self.fitness=HEIGHT*1/distance(self.posx,self.posy,target[0].posx,target[0].posy)
        if self.fitness > maxFitness:
            maxFitness = self.fitness
            print(self.fitness,maxFitness)
        
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

rockets=[]
NumberOfRockets = 10
for i in range(NumberOfRockets):
    rockets.append(Rocket(random()*WIDTH, random()*HEIGHT))

target=[]
target.append(Target(floor(WIDTH/2),20))

while True:
    DeadRockets = []
    Counter += 1
    
    if Counter == LifeSpan:
        print("restarting...")
        for i, rocket in enumerate(rockets):
            rocket.calcFitness()
        time.sleep(2)
        Counter = 0
        maxFitness = 0
        canvas.delete(ALL)
        del target
        target=[]
        target.append(Target(floor(WIDTH/2),20))
        del rockets
        rockets=[]
        for i in range(NumberOfRockets):
            rockets.append(Rocket(random()*WIDTH, random()*HEIGHT))            

    for i, rocket in enumerate(rockets):
        rocket.update()
        if rocket.RocketAlive == False:
            DeadRockets.append(i)

    for i in DeadRockets:
        print(i, " is dead, cleaning...")
        time.sleep(0.1)
        canvas.delete(rockets[i].shape)
        del rockets[i]
        rockets.append(Rocket(random()*WIDTH, random()*HEIGHT))
    
    tk.update()
    time.sleep(0.1)

tk.mainloop()
