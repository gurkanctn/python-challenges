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
## DONE (15.06): Perlin Noise implemented (credits: XXXX)

from tkinter import *
import time, timeit
from random import *
#import gurkan as gg
import math
from math import sin, cos
from perlin_noise import *

WIDTH  = 400
HEIGHT = 400

tk = Tk()
canvas = Canvas(tk, width = WIDTH, height = HEIGHT, bg="black")
tk.title("Random Flow in Perlin Flow Field")
canvas.pack()

def pixel(x,y):
    x=math.floor(x)
    y=math.floor(y)
    #col=[a+b for a,b in zip(list(img.get(x,y)),[20,20,20])]
    col=('#%02X%02X%02X' % (200,200,200)) #col[0],col[1],col[2]))
    if x>=0 and y>=0:
        img.put(col,(x,y))

class Particle:
    def __init__(self,x,y):
        self.posx = random()*WIDTH
        self.posy = random()*HEIGHT
        #self.shape=gg.circle(canvas,self.posx,self.posy,2,"white","c")
        pixel(self.posx,self.posy)  # pixel is faster than self.shape
        self.xvel = 0
        self.yvel = 0
        self.die=False
        
    def move(self):
        #canvas.move(self.shape, self.xvel, self.yvel)
        self.posx = self.posx + self.xvel
        self.posy = self.posy + self.yvel
        #pos=canvas.coords(self.shape)
        if self.posy >= HEIGHT or self.posy <=0:
            self.die=True
        elif self.posx >= WIDTH or self.posx <=0:
            self.die=True
        else:
            self.xvel += pgrid*sin(vector[math.floor(self.posx*pgrid)][math.floor(self.posy*pgrid)])
            self.yvel += pgrid*cos(vector[math.floor(self.posx*pgrid)][math.floor(self.posy*pgrid)])
        pixel(self.posx,self.posy)

    #def trail(self):
        #pos=canvas.coords(self.shape)
    #    pixel(self.posx,self.posy)

r = lambda: randint(40,255)

## ............................................ ##

grid = 20   # Grid size
pgrid=1/grid
cols = math.floor(WIDTH*pgrid)
rows = math.floor(HEIGHT*pgrid)
pcols =math.floor(1/cols)
prows =math.floor(1/rows)

# Create a list.
vector = [[0 for j in range(cols)] for i in range(rows)]

vector2d=perlin_noise(cols,rows,4)
for i in range(cols):
    for j in range(rows):
        #print (i, j)
        a = vector2d[0][i][j]   # maybe i and j should be reverse
        vector[i][j]=a*2*pi
    print(vector[i])


#Show Vectors as lines
for y in range(rows):
    for x in range(cols):
        c=canvas.create_line(x+x*grid,
                             y+y*grid,
                             x+x*grid + grid*sin(vector[x][y]),
                             y+y*grid + grid*cos(vector[x][y]),
                             fill="red", width=2)
        #print(x*grid,y*grid,x+x*grid+6*sin(vector[x][y]),y+y*grid+6*sin(vector[x][y]))



#canvas.itemconfig(ALL,fill="white")
tk.update()
#time.sleep(0.01)

img = PhotoImage(width=WIDTH, height=HEIGHT)
canvas.create_image((WIDTH*0.5, HEIGHT*0.5), image=img, state="normal")

particles=[]
for i in range(100):
    particles.append(Particle(random()*WIDTH, random()*HEIGHT))

ttt=0
while ttt<50000:
    ttt=ttt+1
    ddel=-1
    #t1=time.process_time()
    for i, particle in enumerate(particles):
        particle.move()
        if particle.die:
            ddel=i
        #else:
        #    particle.trail()
    if ddel != -1:
        #canvas.delete(particles[ddel].shape)
        del particles[ddel]
        ddel=-1
        particles.append(Particle(random()*WIDTH,random()*HEIGHT))
    tk.update()
    #t2=time.process_time()
    #if t2!=t1: print(1/(t2-t1))
    # time.sleep(0.01)

tk.mainloop()      

