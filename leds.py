# SIT210 Task 5.1P
# Simple Tkinter GUI to control 3 LEDs (Red, Green, Blue) on Raspberry Pi

import tkinter as tk
import RPi.GPIO as GPIO

# Pin numbers for LEDs (BCM mode)
RED = 17
GREEN = 27
BLUE = 22
PINS = [RED, GREEN, BLUE]

# Setup GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
for pin in PINS:
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, GPIO.LOW)

# Functions
def turn_on(color_pin):
    for pin in PINS:
        GPIO.output(pin, GPIO.LOW)
    GPIO.output(color_pin, GPIO.HIGH)

def on_exit():
    for pin in PINS:
        GPIO.output(pin, GPIO.LOW)
    GPIO.cleanup()
    root.destroy()

# GUI
root = tk.Tk()
root.title("LED Controller")

label = tk.Label(root, text="Choose an LED to turn ON", font=("Arial", 12))
label.pack(pady=10)

# Radio buttons
choice = tk.StringVar()

tk.Radiobutton(root, text="Red", variable=choice, value="red",
               command=lambda: turn_on(RED)).pack(anchor="w")
tk.Radiobutton(root, text="Green", variable=choice, value="green",
               command=lambda: turn_on(GREEN)).pack(anchor="w")
tk.Radiobutton(root, text="Blue", variable=choice, value="blue",
               command=lambda: turn_on(BLUE)).pack(anchor="w")

# Exit button
exit_button = tk.Button(root, text="Exit", command=on_exit)
exit_button.pack(pady=10)

root.protocol("WM_DELETE_WINDOW", on_exit)
root.mainloop()
