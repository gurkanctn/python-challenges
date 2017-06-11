## Gürkan Çetin, 11 June 2017
## GitHub/gurkanctn
##
## Start : 14:24
## End   : 16:00
## inspired from David Shiffman's video: https://www.youtube.com/watch?v=BjoM9oKOAKY
## unfortunately the randomness is not Perlin noise. It will require setting up
## some perlinnoise function.. Which I don't have time for.
## I found one on github, but it doesn't seem to work.
##
## TODO: leaving traces would be a nice visualization


from tkinter import *
import time
import random
import gurkan as gg
import math

WIDTH  = 400
HEIGHT = 400

tk= Tk()
canvas = Canvas(tk, width = WIDTH, height = HEIGHT, bg="black")
tk.title("Gürkan")
canvas.pack()

# gg.circle(canvas, 100,100,10,"red","circle1")

## the whole screen will be a grid containing flow-field vectors
## those vectors will push the flow particles.

class Particle:
    def __init__(self,x,y):
        self.shape=gg.circle(canvas,random.random()*WIDTH,random.random()*HEIGHT,2,"white","c")
        self.xvel = (random.random()*4-2)
        self.yvel = (random.random()*4-2)
        self.die=False
        
    def move(self):
        canvas.move(self.shape, self.xvel, self.yvel)
        pos=canvas.coords(self.shape)
        if pos[3] >= HEIGHT or pos[1] <=0:
            self.die=True
        elif pos[2] >= WIDTH or pos[0] <=0:
            self.die=True
        else:
            self.xvel += vectorx[math.floor(pos[0]/grid)]/grid
            self.yvel += vectory[math.floor(pos[1]/grid)]/grid

grid = 20
cols = WIDTH/grid
rows = HEIGHT/grid
vectorx = []
vectory = []

r = lambda: random.randint(40,255)

for y in range(grid):
    for x in range(grid):
        #col=('#%02X%02X%02X' % (r(),r(),r()))
        #vector[x+y*grid]=
        #print(x,y, x+y*grid, col)
        #c=canvas.create_rectangle(x*grid,y*grid,x*grid+1,y*grid+1,fill="red")
        #gg.circle(canvas,x*grid,y*grid,grid/2,col,"tag")
        vectorx.append(random.random()-0.5)
        vectory.append(random.random()-0.5)

# Show Vectors as lines
#for y in range(grid):
#    for x in range(grid):
#        c=canvas.create_line(x+x*grid,y+y*grid,x+x*grid+vectorx[x+y*grid]*grid*0.5,y+y*grid+vectory[x+y*grid]*grid*0.5, fill="white")
#        print(x*grid,y*grid,x+vectorx[x+y*grid],y+vectory[x+y*grid])

canvas.itemconfig(ALL,fill="white")
tk.update()
#time.sleep(0.01)

particles=[]

for i in range(400):
    particles.append(Particle(random.random()*WIDTH,random.random()*HEIGHT))

while True:
    ddel=-1
    for i, particle in enumerate(particles):
        particle.move()
        if particle.die:
            ddel=i
    if ddel != -1:
        canvas.delete(particles[ddel].shape)
        del particles[ddel]
        ddel=-1
        particles.append(Particle(random.random()*WIDTH,random.random()*HEIGHT))
    tk.update()
    # time.sleep(0.01)
    
tk.mainloop()
tk.destroy()        

