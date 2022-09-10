import tkinter as tk
from tkinter import ttk

class Settings(ttk.Frame):
    def __init__(self, parent, controller,show_timer):
        super().__init__(parent)

        self["style"] ="Background.TFrame"

        settings_container = ttk.Frame(self,style="Background.TFrame")
        settings_container.grid(row=0, column=0,padx=20,pady=20, sticky="NSEW")

        pomodoro_label = ttk.Label(settings_container,
                                   text ="Time for Pomodoro",
                                   style="LightText.TLabel"
                                   )
        pomodoro_label.grid(row=0, column =0,sticky="W")

        pomodoro_input = tk.Spinbox(settings_container,
                                    textvariable=controller.pomodoro,
                                    from_=1,to = 120,
                                    increment=1,
                                    justify ="center",
                                    width=10)
        pomodoro_input.grid(row=0, column=1,sticky="EW")

        longbreak_label = ttk.Label(settings_container,
                                   text="Time for Long break",
                                    style="LightText.TLabel",
                                    )
        longbreak_label.grid(row=1, column=0, sticky="W")
        longbreak_input = tk.Spinbox(settings_container,
                                    textvariable=controller.long_break,
                                    from_=1, to=60,
                                    increment=1,
                                    justify="center",
                                    width=10)
        longbreak_input.grid(row=1, column=1, sticky="EW")

        shortbreak_label = ttk.Label(settings_container,
                                    text="Time for Short break",
                                     style="LightText.TLabel"
                                    )
        shortbreak_label.grid(row=2, column=0, sticky="W")
        shortbreak_input = tk.Spinbox(settings_container,
                                    textvariable=controller.short_break,
                                     from_=1, to=60,
                                     increment=1,
                                     justify="center",
                                     width=10)
        shortbreak_input.grid(row=2, column=1, sticky="EW")

        button_container = ttk.Frame(self)
        button_container.grid(row=1, column=0, sticky="NSEW")
        button_container.columnconfigure(0,weight=1)
        back_button = ttk.Button(button_container,
                                 text= "Back",
                                 command= show_timer,
                                 style="PomButton.TButton"
                                 )
        back_button.grid(sticky="NSEW")

        for child in settings_container.winfo_children():
            child.grid_configure(padx=10, pady=10)


