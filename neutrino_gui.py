import tkinter as tk
from tkinter import ttk
from ttkthemes import *
import sys
import subprocess

window = tk.Tk()

window.title(u"NEUTRINO GUI")
window.geometry("450x450")

menubar = tk.Menu(window)
window.config(menu=menubar)

setting_menu = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label="Settings", menu=setting_menu)
setting_menu.add_command(label="Preferences")
setting_menu.add_command(label="Exit", command=window.quit)

help_menu = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label="Help", menu=help_menu)

file_name = "Run.bat"
key_pitch = {"-6": 0.707, "-5": 0.749, "-4": 0.794, "-3": 0.841, "-2": 0.891, "-1": 0.944,
             "0": 1.000, "1": 1.059, "2": 1.122, "3": 1.189, "4": 1.260, "5": 1.335, "6": 1.414}


def run():
    with open(file_name) as f:
        data_lines = f.read().split("\n")
    for i, item in enumerate(data_lines):
        if "musicxml_filename" in data_lines[i]:
            data_lines[i] = data_lines[i].replace(
                "musicxml_filename", str(entry_filename.get()))
        if "modelname" in data_lines[i]:
            data_lines[i] = data_lines[i].replace(
                "modelname", str(model_val.get()))
            print(data_lines[i])
        if "pitchshift_val" in data_lines[i]:
            data_lines[i] = data_lines[i].replace(
                "pitchshift_val", str(val1.get()))
        if "formantshift_val" in data_lines[i]:
            data_lines[i] = data_lines[i].replace(
                "formantshift_val", str(val2.get()))

    string = "\n".join(data_lines)
    print(data_lines)
    print(string)

    with open(file_name, mode="w") as f:
        f.write(string)

    subprocess.run("Run.bat")


def reset():
    with open("run_init.bat") as f:
        data_lines = f.read()

    with open("run.bat", "w") as f:
        f.write(data_lines)


frame_filename = tk.LabelFrame(
    window, text="MusicXML File Name", foreground="blue", padx=20, pady=20)
frame_filename.grid(row=0, column=0, padx=20, pady=20, sticky=tk.W)
entry_filename = ttk.Entry(frame_filename)
entry_filename.pack(side="left")
label1 = tk.Label(frame_filename, text=".musicxml")
label1.pack(side="left")

frame_pitchshift = tk.LabelFrame(
    window, text="Pitch Shift", foreground="blue", padx=20, pady=20)
frame_pitchshift.grid(row=1, column=0, padx=20, pady=20, sticky=tk.W)
label_pitchshift = tk.Label(frame_pitchshift, text="Key")
label_pitchshift.pack(side="left", padx=5)
val1 = tk.IntVar()
val1.set(0)
spinbox_pitchshift = ttk.Spinbox(
    frame_pitchshift, textvariable=val1, state="readonly", from_=-6, to=6, increment=1)
spinbox_pitchshift.pack(side="left", padx=5)

frame_formantshift = tk.LabelFrame(
    window, text="Formant Shift", foreground="blue", padx=20, pady=20)
frame_formantshift.grid(row=2, column=0, padx=20, pady=20, sticky=tk.W)
val2 = tk.DoubleVar()
val2.set("{:.2f}".format(1.00))
scale_formantshift = tk.Scale(
    frame_formantshift, showvalue=False, orient=tk.HORIZONTAL, sliderrelief=tk.RAISED, variable=val2, length=150, from_=0.85, to=1.15, resolution=0.01)
scale_formantshift.pack(side="left", padx=5)
label_val2 = tk.Label(frame_formantshift, textvariable=val2)
label_val2.pack(side="left", padx=2)

frame_model = tk.LabelFrame(
    window, text="Model", foreground="blue", padx=20, pady=20)
frame_model.grid(row=0, column=1, rowspan=2, padx=20, pady=20, sticky=tk.W)
model_val = tk.StringVar()
model_val.set("KIRITAN")
rb_KIRITAN = ttk.Radiobutton(
    frame_model, variable=model_val, text="KIRITAN", value="KIRITAN")
rb_KIRITAN.pack(anchor=tk.W, padx=5, pady=5)
rb_YOKO = ttk.Radiobutton(
    frame_model, variable=model_val, text="YOKO", value="YOKO")
rb_YOKO.pack(anchor=tk.W, padx=5, pady=5)
rb_ITAKO = ttk.Radiobutton(
    frame_model, variable=model_val, text="ITAKO", value="ITAKO")
rb_ITAKO.pack(anchor=tk.W, padx=5, pady=5)
rb_JSUT = ttk.Radiobutton(
    frame_model, variable=model_val, text="JSUT", value="JSUT")
rb_JSUT.pack(anchor=tk.W, padx=5, pady=5)
rb_NAKUMO = ttk.Radiobutton(
    frame_model, variable=model_val, text="NAKMUO", value="NAKUMO")
rb_NAKUMO.pack(anchor=tk.W, padx=5, pady=5)
rb_MERROW = ttk.Radiobutton(
    frame_model, variable=model_val, text="MERROW", value="MERROW")
rb_MERROW.pack(anchor=tk.W, padx=5, pady=5)


frame_run = tk.Frame(window, padx=20, pady=20)
frame_run.grid(row=2, column=1, padx=20, pady=20, sticky=tk.W)
button_run = tk.Button(frame_run, relief=tk.RAISED,
                       text="Run", width=10, command=run)
button_run.pack(side="top", pady=10)
button_reset = tk.Button(frame_run, relief=tk.RAISED,
                         text="RESET", width=10, command=reset)
button_reset.pack(side="top", pady=10)


window.mainloop()
