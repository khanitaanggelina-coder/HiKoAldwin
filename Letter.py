import turtle as t

# Display
t.speed(3)
t.bgcolor("pink")
t.title("For Ko Aldwin")

# Heart Drawing
t.up()
t.goto(0, -100) 
t.down()
t.color("red")
t.fillcolor("red")
t.begin_fill()

# Heart Drawing
t.left(140)
t.forward(180)
t.circle(-90, 200)
t.setheading(60)
t.circle(-90, 200)
t.forward(180)

t.goto(0, -100)  
t.end_fill()

# Text Writing
t.up()
t.goto(0, 10)  
t.down()
t.color("lightblue")
t.write("Hey njink", align="center", font=("Verdana", 20, "bold"))

t.ht() 
t.mainloop()   