import tkinter as tk
# from tkinter import ttk
import ttkbootstrap as ttk

# -> The default conversion direction is MINUTES TO HOURS.

# -----------
# Structure
# -----------
window = ttk.Window(themename="morph")

window.title("Time Converter")  # -> Window's title
window.geometry("800x400")  # -> Window's dimension

# -----------
# Functions
# -----------


def set_min_hr():
    """Set minutes to hours
    """
    button.configure(command=convert_min_hr)


def set_hr_min():
    """Set hours to minutes
    """
    button.configure(command=convert_hr_min)


def convert_hr_min():
    """Convert hours to minutes

    Return
    ------
        * float : Display the convertion between hours and minutes
    """
    value = var_entry.get()  # -> get entry value
    calc_hr_min = value * 60  # -> calcul the convertion
    var_value.set(calc_hr_min)  # -> set the output value


def convert_min_hr():
    """Convertion de heur à minute

    Sortie
    ------
        * float : Display the convertion between minutes and hours
    """
    value = var_entry.get()  # -> get entry value
    calc_min_hr = value / 60  # -> calcul the convertion
    var_value.set(calc_min_hr)  # -> set the output value

# -----------
# Tkinter variable
# -----------


var_entry = tk.IntVar(value=0)  # -> Entry's User variable
var_value = tk.IntVar(value=0)  # -> Output's value variable
var_radio = tk.IntVar()  # -> Radio's values variable (1 or 2)

# -----------
# Widgets
# -----------

# Information
information = ttk.Label(
    window, text="The default conversion direction is MINUTES TO HOURS. These are integer values only.")
information.pack(pady=5)

# Logiciel title
title_logiciel = ttk.Label(
    window, text="Time Converter", font="Montserrat 20 bold")
title_logiciel.pack()
# Input box

input_box = ttk.Frame(window)
# -> The frame with [User Entry] and [Convert Button]
entry = ttk.Entry(input_box, textvariable=var_entry,
                  font="Montserrat 13 bold")  # -> User Entry
button = ttk.Button(input_box, text="Convert",
                    padding=(30, 10), command=convert_min_hr)  # -> Convert button

input_box.pack(pady=40)
entry.pack(side="left", padx=10)
button.pack(side="left")

# Output box
output_box = ttk.Frame(window)
# -> The output frame with [Output_Label_Title] and [Output_Value]
output_label_title = ttk.Label(
    output_box, text="Output", font="Montserrat 20")  # -> Output Title
output_value = ttk.Label(
    output_box, textvariable=var_value, font="Montserrat 18 bold")  # -> Output value

output_box.pack(pady=25)
output_label_title.pack()
output_value.pack()

# Radios
radio_box = ttk.Frame(window)
# -> The radio frame with [Radio_Min_Hr] and [Radio_Hr_Min]
radio_min_hr = ttk.Radiobutton(
    window, text="Min to Hour", value=1, variable=var_radio, command=set_min_hr)  # -> Radio minute to hours
radio_hr_min = ttk.Radiobutton(
    window, text="Hour to Min", value=2, variable=var_radio, command=set_hr_min)  # -> Rasio hour to minutes

radio_box.pack()
radio_min_hr.pack()
radio_hr_min.pack()

# -----------
# Run
# -----------
window.mainloop()
