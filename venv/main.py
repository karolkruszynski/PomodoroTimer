from tkinter import *
import math
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

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- #

def start_timer():
    global reps
    reps += 1
    work_sec = 5
    short_break_sec = 2
    long_break_sec = 3

    if reps % 2 != 0:
        count_down(work_sec)
        timer.config(fg=GREEN, text="WORK")
    elif reps == 8:
        count_down(long_break_sec)
        timer.config(fg=RED, text="BREAK")
    elif reps % 2 == 0:
        count_down(short_break_sec)
        timer.config(fg=PINK, text="BREAK")


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):

    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec == 0:
        count_sec = "00"
    elif count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        window.after(1000, count_down, count - 1)
    else:
        start_timer()

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro Timer")
window.config(padx=100, pady=50, bg=YELLOW)


canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 111, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

timer = Label(text="TIMER", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 40, "italic"))
timer.grid(column=1, row=0)

start = Button(text="START", command=start_timer, highlightthickness=0)
start.grid(column=0,row=2)

reset = Button(text="RESET", highlightthickness=0)
reset.grid(column=2, row=2)

checker = Label(text="✅", bg=YELLOW, fg=GREEN)
checker.grid(column=1, row=3)





window.mainloop()