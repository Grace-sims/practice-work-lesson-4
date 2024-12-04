import turtle as t

t.speed ()

t.width (2)

t.penup ()
t.forward (200)
t.pendown ()

t.penup ()
t.left (180)
t.pendown ()

for x in range (3):
    t.forward (100)
    t.right (120)
t. end_fill ()

t.penup ()
t.right (180)
t.forward (110)
t.left (180)
t.pendown ()

for x in range (4):
    t.forward (100)
    t.right (90)
t. end_fill ()

t.penup ()
t.forward (220)
t.pendown ()

for x in range (5):
    t.forward (100)
    t.right (72)
t. end_fill ()

t.penup ()
t.forward (210)
t.right (180)
t.pendown ()

for x in range (36):
    t.forward (10)
    t.left(10)
t.end_fill ()

t.penup ()
t.left (180)
t.forward (100)
t.pendown ()

for x in range (6):
    t.forward (80)
    t.right (60)
t. end_fill ()

t.mainloop ()