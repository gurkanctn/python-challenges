"""
http://www.deprem.gov.tr/earthquake/eventfile?lastDay=30&m1=3&type=1&lang=tr
"""

import csv
from tkinter import *
import time, timeit
from random import *
from math import *
from math import sin, cos

tk = Tk()
earthquakes = []
WIDTH  = 897
HEIGHT = 460
##eventList_20171229
with open('2023-02-06.csv', newline='') as f:
    #Tarih(TS),Enlem,Boylam,Derinlik(Km),Tip,Büyüklük,Yer,Deprem Id
    reader = csv.reader(f)
    for row in reader:
        earthquakes.append(row)

canvas = Canvas(tk, width = WIDTH, height = HEIGHT, bg="black")
tk.title("Turkish Earthquakes")
img = PhotoImage(file="TR.gif")
selfphoto = canvas.create_image(0,0, image=img, state="normal", anchor="nw")
canvas.pack()
tk.update()


def ellipse(w,x,y,r,col,t):
## draws a circle, centered at x,y, with radius r
## on canvas w
## with color = col; as a col hex code string
## tagged t
    id=w.create_oval(x-r,y-r,x+r,y+r,fill=col,tag=t)

def ll2xy(lat,lon):
    #(lat, lon) = (38.283157, 26.278373) = İzmir batı ucu = (x,y) = (56, 263)
    #(lat, lon) = (39.912954, 32.782739) = Ankara merkez = (x,y) = (325, 176)
    #(lat, lon) = (37.200750, 44.766408) = Hakkari Ucu = (x,y) = (824, 322)
    #(lat, lon) = (42.101058, 34.959371) = sinop Ucu = (x,y) = (418, 58)
    newx = 56 + (lon - 26.278373) * (824-56)/(44.766408-26.278373)
    newy = 58 + (lat - 42.101058) * (322-58)/(37.200750-42.101058)
    #myx = 117 + ((lon - 27.7666) * (43.478))
    #myy = 378 + (lat-36.1348)*(-52.87233763)
    return (newx,newy)

class Quake:
    def __init__(self,x,y,r,c):
        self.posx = x
        self.posy = y
        ##col=[min((a+b),255) for a,b in zip(list(img.get(self.posx,self.posy)),[0,0,0])]
        ##col=('#%02X%02X%02X' % (col[0],col[1],col[2]))
        col=('#%02X%02X%02X' % (255-c,c,255-c))
        self.col=col
        self.r = 0.7*r**1.5  ##r*r*0.4   TODO: PLAY WITH IT
        self.shape = ellipse(canvas,x,y,self.r,self.col,"c")

quakes = []
for i in range(1,len(earthquakes)):
    if i == 0: continue
    mag=float(earthquakes[i][5])
    if mag >= 3.00:     ## ignore all quakes that mag <3.
        lat = float(earthquakes[i][1])
        lon = float(earthquakes[i][2])
        (x,y)=ll2xy(lat,lon)
        ##print(x,y)
        quakes.append(Quake(x,y,0.2*(mag**2),int(mag**3))) ## the last argument is for coloring!


lats = []
##lats.append(39.480476)
lats.append(41.148996)
lats.append(35.928875)

lons = []
##lons.append(26.078656)
lons.append(43.478091)
lons.append(27.76666)

x = []
##x.append(51)
x.append(768)
x.append(117)

y = []
##y.append(200)
y.append(112)
y.append(388)

gooda = []
goodb = []
goodc = []

col = ('#%02X%02X%02X' % (255,0,255))
ooo = [True, True]
x2 = [0,0]
y2 = [0,0]

treshold =10
best = treshold

for l in range(100):
    #print(l)
    for k in range(21):
        thisgood = False
        for j in range(11):
            a = 0 # j*0.05-5
            b = 0 #k*0.125-1.5
            c = 0 #l*0.0125-0.725
            for i in range(len(lons)):
                (x2[i],y2[i])=ll2xy(lats[i],lons[i])
            m = ((y2[0]-y[0])**2) 
            n = ((y2[1]-y[1])**2)
            if (max(m,n)<treshold):
                thisgood = True
                if min(m,n)<best:
                    best = min(m,n)
                    print("new best found!: ", l,k,j,best)
        if thisgood:
            gooda.append(a)
            goodb.append(b)
            goodc.append(c)
##            ellipse(canvas,gooda[len(gooda)-1]*4,gooda[len(goodb)-1]*4,2,col,"tag")   
                    
##    quakes.append(Quake(x[i],y[i],x[i]%255))
##    quakes.append(Quake(x2,y2,x[i]%255))
print("finished, %Y found : ", len(gooda))
print("best", best)

if len(gooda)<30:
    print([gooda, goodb, goodc])

if len(gooda)>0:
    print("max:",max(gooda),max(goodb),max(goodc))
    print("min:",min(gooda),min(goodb),min(goodc))
    print("avg:",0.5*(max(gooda)+min(gooda)),
          0.5*(max(goodb)+min(goodb)),
          0.5*(max(goodc)+min(goodc)))
print(y2,y)
tk.mainloop()

