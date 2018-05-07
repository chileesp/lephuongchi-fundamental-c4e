from turtle import *

def draw_star (x,y,z):
    for i in range (x):
        forward (z)
        right (y*360.0/x)
draw_star (5,2,100)


speed(0)
color('blue')
for i in range(100):
    import random
    x = random.randint(-300, 300)
    y = random.randint(-300, 300)
    length = random.randint(3, 10)
    draw_star(x, y, length)

mainloop()
