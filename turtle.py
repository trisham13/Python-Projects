import turtle

t=turtle.Pen()

t.forward(50);
t.left(90);
t.forward(50);
t.left(90);
t.forward(50);
t.left(90);
t.forward(50);
t.left(90);
t.reset();
t.backward(100);
t.up();
t.right(90);
t.forward(20);
t.right(90);
t.down();
t.backward(100);
t.right(90);
t.forward(20);
t.up();
t.left(90);
t.forward(100);
t.left(90);
t.down();
t.forward(20);
t.reset();
t.forward(100);
t.left(120);
t.forward(100);
t.left(120);
t.forward(100);
t.reset();
for x in range(4):
    t.forward(50);
    t.up();
    t.forward(10);
    t.left(90);
    t.forward(10);
    t.down();
t.reset();
for x in range (0,5):
    t.forward(100);
    t.left(144);
t.reset();
t.color("blue");
t.pensize(5);
for x in range (1,19):
    t.forward(100);
    if x % 2 == 0:
        t.left(175);
    else:
        t.left(225);
        
t.reset();
t.color(1,1,0);
t.begin_fill();
t.circle(50);
t.end_fill();
