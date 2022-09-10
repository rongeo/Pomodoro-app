import tkinter as tk
from tkinter import ttk
from collections import deque
from timer import Timer
from settings import Settings
from windowsdpi import set_dpi_awarness
from colour import Colour


set_dpi_awarness()



#styling UI with colours
selected_colour= Colour()

i=5
colour_primary=selected_colour.combinations[i]["colour_primary"]
colour_secondary=selected_colour.combinations[i]["colour_secondary"]
colour_light_background=selected_colour.combinations[i]["colour_light_background"]
colour_light_text=selected_colour.combinations[i]["colour_light_text"]
colour_dark_text=selected_colour.combinations[i]["colour_dark_text"]



class Pomodorotimer(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args,**kwargs)

        style = ttk.Style(self)
        style.theme_use("clam")
        style.configure("Timer.TFrame", background=colour_light_background)
        style.configure("Background.TFrame", background=colour_primary)
        style.configure("TimerText.TLabel",
                        background=colour_light_background,
                        foreground=colour_dark_text,
                        font="Helvetica 36"
                        )
        style.configure("LightText.TLabel",
                        background=colour_primary,
                        foreground=colour_light_text,
                        )
        style.configure("PomButton.TButton",
                        background=colour_primary,
                        foreground=colour_light_text)
        style.map("PomButton.TButton",
                  background=[("active",colour_secondary),("disabled",colour_light_text)])

        self["background"]=colour_primary

        self.title("Pomodoro Timer")
        self.columnconfigure(0,weight=1)

        self.pomodoro= tk.StringVar(value=25)
        self.long_break= tk.StringVar(value=10)
        self.short_break= tk.StringVar(value=5)
        self.timer_order = ["Pomodoro", "Short Break", "Pomodoro", "Short Break", "Pomodoro", "Long Break"]
        self.timer_schedule = deque(self.timer_order)

        container = ttk.Frame(self)
        container.grid()

        self.frames = dict()


        settings_frame = Settings(container,self,lambda:self.show_frames(Timer))
        settings_frame.grid(row=0, column=0, sticky="NSEW")
        timer_frame = Timer(container, self, lambda: self.show_frames(Settings))
        timer_frame.grid(row=0, column=0, sticky="NSEW")

        self.frames[Timer] = timer_frame
        self.frames[Settings] = settings_frame


    def show_frames(self,selected_frame):
        frame = self.frames[selected_frame]
        frame.tkraise()




window= Pomodorotimer()

window.mainloop()