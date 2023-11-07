import tkinter as tk
import random

def move_ball():
    global ball_x, ball_y, ball_dx, ball_dy
    canvas.delete("ball")
    ball_x += ball_dx
    ball_y += ball_dy
    if ball_x >= WIDTH - BALL_RADIUS or ball_x <= 0:
        ball_dx = -ball_dx
        change_color()
    if ball_y >= HEIGHT - BALL_RADIUS or ball_y <= 0:
        ball_dy = -ball_dy
        change_color()
    canvas.create_oval(ball_x, ball_y, ball_x + BALL_RADIUS*2, ball_y + BALL_RADIUS*2, fill=ball_color, tags="ball")
    window.after(DELAY, move_ball)

def change_color():
    global ball_color
    ball_color = random.choice(COLORS)

WIDTH, HEIGHT = 600, 400  
BALL_RADIUS = 15  
COLORS = ["red", "green", "blue", "yellow", "pink", "orange"]
ball_x, ball_y = random.randint(BALL_RADIUS, WIDTH - BALL_RADIUS), random.randint(BALL_RADIUS, HEIGHT - BALL_RADIUS)
ball_dx, ball_dy = random.randint(-5, 5), random.randint(-5, 5)  
ball_color = random.choice(COLORS)
DELAY = 25  

window = tk.Tk()
window.title("Bouncing Ball")

canvas = tk.Canvas(window, width=WIDTH, height=HEIGHT, bg="white")
canvas.pack()

move_ball()

window.mainloop()
