from turtle import *

def draw_star (x,y,z):
    for i in range (x):
        forward (z)
        right (y*360.0/x)
draw_star (5,2,100)

mainloop()
