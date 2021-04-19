from tkinter import *
import math

PINK = "#e2979c"
RED = "e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_DURATION = 1500
SHORT_BREAK_DURATION = 300
LONG_BREAK_DURATION = 1200
rounds = 0


def start_timer():
    global rounds
    rounds += 1
    count_down(WORK_DURATION)
    if rounds % 8 == 0:
        count_down(LONG_BREAK_DURATION)
        title_label.config(text="Break", fg=RED)
    elif rounds % 2 == 0:
        count_down(SHORT_BREAK_DURATION)
        title_label.config(text="Break", fg=PINK)
    else:
        count_down(WORK_DURATION)
        title_label.config(text="Work", fg=GREEN)


def count_down(count):
    minutes = math.floor(count / 60)
    seconds = count % 60
    if seconds < 10:
        seconds = f"0{seconds}"

    canvas.itemconfig(timer_text, text=f"{minutes}:{seconds}")

    if count > 0:
        window.after(1000, count_down, count - 1)
    else:
        start_timer()


window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

title_label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50))
title_label.grid(column=1, row=0)

image = PhotoImage(file="tomato.png")
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
canvas.create_image(100, 112, image=image)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

start_button = Button(text="Start", highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", highlightthickness=0)
reset_button.grid(column=2, row=2)

check_marks = Label(text="✓", fg=GREEN, bg=YELLOW)
check_marks.grid(column=1, row=3)

window.mainloop()
