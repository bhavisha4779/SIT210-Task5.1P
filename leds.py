import tkinter as tk
import RPi.GPIO as GPIO

# Use BCM pin numbers
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# Define LED pins
RED, GREEN, BLUE = 17, 27, 22
PINS = [RED, GREEN, BLUE]

# Setup pins as output and turn them off
for pin in PINS:
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, 0)

# Function to turn on one LED at a time
def turn_on(pin):
    for p in PINS:
        GPIO.output(p, 0)  # turn all off
    GPIO.output(pin, 1)    # turn selected on

# Cleanup on exit
def on_exit():
    for p in PINS:
        GPIO.output(p, 0)
    GPIO.cleanup()
    root.destroy()

# GUI setup
root = tk.Tk()
root.title("LED Controller")

tk.Label(root, text="Select an LED:").pack()

# Radio buttons
tk.Radiobutton(root, text="Red", command=lambda: turn_on(RED)).pack(anchor="w")
tk.Radiobutton(root, text="Green", command=lambda: turn_on(GREEN)).pack(anchor="w")
tk.Radiobutton(root, text="Blue", command=lambda: turn_on(BLUE)).pack(anchor="w")

# Exit button
tk.Button(root, text="Exit", command=on_exit).pack(pady=10)

# Handle window close
root.protocol("WM_DELETE_WINDOW", on_exit)

# Start GUI loop
root.mainloop()

