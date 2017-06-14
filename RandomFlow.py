## Gürkan Çetin, 11 June 2017
## GitHub/gurkanctn
##
## Start : 14:24
## End   : 16:00
## inspired from Daniel Shiffman's video: https://www.youtube.com/watch?v=BjoM9oKOAKY
## unfortunately the randomness is not Perlin noise. I found out that
## it will require setting up
## some perlin noise function. Which I don't have time for.
## I found one on github, but it doesn't seem to work.
##
## TODO:
## DONE (14.06): leaving traces would be a nice visualization.it will probably
## crash after running a long while (because of the "col" list overflowing...

from tkinter import *
import time, timeit
import random
import gurkan as gg
import math
from math import sin

WIDTH  = 400
HEIGHT = 400

tk= Tk()
canvas = Canvas(tk, width = WIDTH, height = HEIGHT, bg="black")
tk.title("Gürkan")
canvas.pack()

# gg.circle(canvas, 100,100,10,"red","circle1")

## the whole screen will be a grid containing flow-field vectors
## those vectors will push the flow particles.

def pixel(x,y):
    x=math.floor(x)
    y=math.floor(y)
    #col=[a+b for a,b in zip(list(img.get(x,y)),[20,20,20])]
    col=('#%02X%02X%02X' % (200,200,200)) #col[0],col[1],col[2]))
    img.put(col,(x,y))   

class Particle:
    def __init__(self,x,y):
        self.shape=gg.circle(canvas,random.random()*WIDTH,random.random()*HEIGHT,2,"white","c")
        self.xvel = (random.random()*6-3)
        self.yvel = (random.random()*6-3)
        self.die=False
        
    def move(self):
        canvas.move(self.shape, self.xvel, self.yvel)
        pos=canvas.coords(self.shape)
        if pos[3] >= HEIGHT or pos[1] <=0:
            self.die=True
        elif pos[2] >= WIDTH or pos[0] <=0:
            self.die=True
        else:
            self.xvel += vectorx[math.floor(pos[0]/grid)]
            self.yvel += vectory[math.floor(pos[1]/grid)]

    def trail(self):
        pos=canvas.coords(self.shape)
        pixel(0.5*(pos[0]+pos[2]),0.5*(pos[1]+pos[3]))

r = lambda: random.randint(40,255)

## ............................................ ##

grid = 20
cols = WIDTH/grid
rows = HEIGHT/grid
vectorx = []
vectory = []


for y in range(grid):
    for x in range(grid):
        vectorx.append(random.random()-0.5)
        vectory.append(random.random()-0.5)

#Show Vectors as lines
#for y in range(grid):
#    for x in range(grid):
#        c=canvas.create_line(x+x*grid,y+y*grid,x+x*grid+vectorx[x+y*grid]*grid*0.5,y+y*grid+vectory[x+y*grid]*grid*0.5, fill="white")
#        print(x*grid,y*grid,x+vectorx[x+y*grid],y+vectory[x+y*grid])

canvas.itemconfig(ALL,fill="white")
tk.update()
#time.sleep(0.01)

img = PhotoImage(width=WIDTH, height=HEIGHT)
canvas.create_image((WIDTH/2, HEIGHT/2), image=img, state="normal")

particles=[]
for i in range(100):
    particles.append(Particle(random.random()*WIDTH,random.random()*HEIGHT))

while True:
    ddel=-1
    #t1=time.process_time()
    for i, particle in enumerate(particles):
        particle.move()
        if particle.die:
            ddel=i
        else:
            particle.trail()
    if ddel != -1:
        canvas.delete(particles[ddel].shape)
        del particles[ddel]
        ddel=-1
        particles.append(Particle(random.random()*WIDTH,random.random()*HEIGHT))
    tk.update()
    #t2=time.process_time()
    #if t2!=t1: print(1/(t2-t1))
    # time.sleep(0.01)

tk.mainloop()
tk.destroy()        

