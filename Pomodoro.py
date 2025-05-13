from tkinter import *
#Main window
root = Tk()
root.title("Pomodoro")
root.geometry("700x700")

#Time Variable
time_left = 0
paused = False

#Variable to hold the selected mode
value = StringVar(value="Pomodoro")

#Function that toggles between sections
def change_mode():
    global time_left
    if value.get() == "Pomodoro":
        timer.config(text="25:00")
        time_left = 25 * 60
    elif value.get() == "Short Break":
        timer.config(text="05:00")
        time_left = 5 * 60
    elif value.get() == "Long Break":
        timer.config(text="15:00")
        time_left = 15 * 60
    update_mode_label()
        
#Mode Change
mode_Text = StringVar(value=f"MODE: {value.get()}")

def update_mode_label():
    mode_Text.set(f"MODE: {value.get()}")

#Timer Logic
def countdown():
    global time_left, paused
    if not paused:
        minute = time_left // 60
        seconds = time_left % 60

        timer.config(text=f"{minute:02d}:{seconds:02d}")
    
        if time_left > 0:
            time_left -= 1
            R1.config(state=DISABLED)
            R2.config(state=DISABLED)
            R3.config(state=DISABLED)
            root.after(1000,countdown)
        else:
            R1.config(state=NORMAL)
            R2.config(state=NORMAL)
            R3.config(state=NORMAL)
            status_label.config(text="Time's Up")
            start.config(state=NORMAL)

def pausedown():
    global paused
    paused = True
    
def stopdown():
    global time_left, paused
    paused = True
    time_left=0
    change_mode()
    R1.config(state=NORMAL)
    R2.config(state=NORMAL)
    R3.config(state=NORMAL)
    
#Timer Click
def timer_click(action):
    if action == "Start":
        global paused
        paused = False
        if time_left == 0:
            change_mode()
        status_label.config(text="Timer Started")
        start.config(state=DISABLED)
        pause.config(state=NORMAL)
        stop.config(state=NORMAL)
        countdown()
    elif action=="Pause":
        status_label.config(text="Timer Paused")
        start.config(state=NORMAL)
        pause.config(state=DISABLED)
        stop.config(state=NORMAL)
        pausedown()
    elif action=="Stop":
        status_label.config(text="Timer Stopped")
        start.config(state=NORMAL)
        pause.config(state=DISABLED)
        stop.config(state=DISABLED)
        stopdown()
        change_mode()
    update_mode_label()

#Label
label = Label(root,text="Welcome to Pomodoro App", font=("Arial",10,"bold"))
label.pack()

radio_frame = Frame(root)
radio_frame.pack(pady=30)

#Radio
#variable attribute to match the selected value
R1 = Radiobutton(radio_frame, text="Pomodoro", value="Pomodoro", variable=value, command=change_mode, font=("serif",13,"italic"))
R1.pack(side="left")
R2 = Radiobutton(radio_frame, text="Short Break", value="Short Break", variable=value, command=change_mode, font=("serif",13,"italic"))
R2.pack(side="left")
R3 = Radiobutton(radio_frame, text="Long Break", value="Long Break", variable=value, command=change_mode, font=("serif",13,"italic"))
R3.pack(side="left")

#Timer Label
timer = Label(root, text="25:00", font=("Arial",40,"bold"))
timer.pack()

#Mode
mode_label = Label(root,textvariable=mode_Text, font=("Arial", 11, "bold"))
mode_label.pack()

button_frame = Frame()
button_frame.pack(pady=30)

#Buttons for Timer
start=Button(button_frame, text="Start", command=lambda:timer_click("Start"), fg="white", bg="green", activebackground="lightgreen", activeforeground="black", font=("sans",12,"bold"))
start.pack(side="left", padx=25, pady=10)

pause=Button(button_frame, text="Pause", command=lambda:timer_click("Pause"), fg="white", bg="orange", activebackground="yellow", activeforeground="black", font=("sans",12,"bold"))
pause.pack(side="left", padx=25, pady=10)
pause.config(state=DISABLED)
stop=Button(button_frame, text="Stop", command=lambda:timer_click("Stop"), fg="white", bg="maroon", activebackground="red", activeforeground="black", font=("sans",12,"bold"))
stop.pack(side="left", padx=25, pady=10)
stop.config(state=DISABLED)

#Status
status_label = Label(root,text="", font=("Arial",11,"bold"))
status_label.pack(pady=5)

#Run
root.mainloop()
