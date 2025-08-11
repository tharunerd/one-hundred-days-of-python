import tkinter as tk
from tkinter import messagebox
import math
import time
import threading
import winsound  # Works on Windows for sound

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global reps
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    title_label.config(text="Timer")
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1

    # Get user input
    try:
        work_sec = int(work_min_input.get()) * 60 + int(work_sec_input.get())
        short_break_sec = int(short_break_min_input.get()) * 60 + int(short_break_sec_input.get())
        long_break_sec = int(long_break_min_input.get()) * 60 + int(long_break_sec_input.get())
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid integers for all time fields.")
        return

    if reps % 8 == 0:
        count_down(long_break_sec, "Long Break", RED)
    elif reps % 2 == 0:
        count_down(short_break_sec, "Short Break", PINK)
    else:
        count_down(work_sec, "Work", GREEN)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count, mode, color):
    minutes = math.floor(count / 60)
    seconds = count % 60
    if seconds < 10:
        seconds = f"0{seconds}"

    canvas.itemconfig(timer_text, text=f"{minutes}:{seconds}")
    title_label.config(text=mode, fg=color)

    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1, mode, color)
    else:
        threading.Thread(target=play_sound).start()
        start_timer()

# ---------------------------- SOUND FUNCTION ------------------------------- #
def play_sound():
    try:
        winsound.Beep(1000, 500)  # Frequency=1000Hz, Duration=500ms
        time.sleep(0.2)
        winsound.Beep(1200, 500)
    except:
        pass

# ---------------------------- UI SETUP ------------------------------- #
window = tk.Tk()
window.title("Pomodoro App")
window.config(padx=100, pady=50, bg=YELLOW)

title_label = tk.Label(text="Timer", fg=GREEN, font=(FONT_NAME, 50, "bold"), bg=YELLOW)
title_label.grid(column=1, row=0)

canvas = tk.Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = tk.PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

# Input fields
tk.Label(text="Work (min)", bg=YELLOW).grid(column=0, row=2)
tk.Label(text="Work (sec)", bg=YELLOW).grid(column=0, row=3)
tk.Label(text="Short Break (min)", bg=YELLOW).grid(column=2, row=2)
tk.Label(text="Short Break (sec)", bg=YELLOW).grid(column=2, row=3)
tk.Label(text="Long Break (min)", bg=YELLOW).grid(column=0, row=4)
tk.Label(text="Long Break (sec)", bg=YELLOW).grid(column=0, row=5)

work_min_input = tk.Entry(width=5)
work_min_input.insert(0, str(WORK_MIN))
work_min_input.grid(column=1, row=2)

work_sec_input = tk.Entry(width=5)
work_sec_input.insert(0, "0")
work_sec_input.grid(column=1, row=3)

short_break_min_input = tk.Entry(width=5)
short_break_min_input.insert(0, str(SHORT_BREAK_MIN))
short_break_min_input.grid(column=3, row=2)

short_break_sec_input = tk.Entry(width=5)
short_break_sec_input.insert(0, "0")
short_break_sec_input.grid(column=3, row=3)

long_break_min_input = tk.Entry(width=5)
long_break_min_input.insert(0, str(LONG_BREAK_MIN))
long_break_min_input.grid(column=1, row=4)

long_break_sec_input = tk.Entry(width=5)
long_break_sec_input.insert(0, "0")
long_break_sec_input.grid(column=1, row=5)

# Buttons
start_button = tk.Button(text="Start", command=start_timer)
start_button.grid(column=0, row=6)

reset_button = tk.Button(text="Reset", command=reset_timer)
reset_button.grid(column=2, row=6)

window.mainloop()
