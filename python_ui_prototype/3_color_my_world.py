import tkinter as tk
import tkinter.ttk as ttk
import customtkinter as ctk
from spinbox import FloatSpinbox
from tkinter import colorchooser

ctk.set_appearance_mode("dark")  # Modes: "System" (standard), "Dark", "Light"
ctk.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"


class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.geometry("1500x800")
        self.title("Python Desktop UI Prototype")

        # set main window grid layout 1x2
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        # create navigation frame
        self.nav_frame = ctk.CTkFrame(self, corner_radius=0)
        self.nav_frame.grid(row=0, column=0, sticky="nsew")
        self.nav_frame.grid_rowconfigure(4, weight=1)

        # Add the shape buttons
        ctk.CTkButton(self.nav_frame, text="Rectangle", command=self.create_rect).pack(padx=5,pady=5,side=ctk.TOP)
        ctk.CTkButton(self.nav_frame, text="Oval", command=self.create_oval).pack(padx=5,pady=5,side=ctk.TOP)
        ctk.CTkButton(self.nav_frame, text="Triangle", command=self.create_triangle).pack(padx=5, pady=5, side=ctk.TOP)
        ctk.CTkButton(self.nav_frame, text="Line", command=self.create_line).pack(padx=5, pady=5, side=ctk.TOP)

        # Add the shape settings
        ctk.CTkLabel(self.nav_frame, text="     ").pack(padx=5, pady=5, side=ctk.TOP)
        ctk.CTkLabel(self.nav_frame, text="Settings").pack(padx=5, pady=5, side=ctk.TOP)

        # create settings frame grid 1x2
        ctk.CTkButton(self.nav_frame, text="Fill Color", command=self.set_fill_color).pack(padx=5,pady=5,side=ctk.TOP)
        self.fill_color_label = ctk.CTkLabel(self.nav_frame, text="", bg_color='white', width=30)
        self.fill_color_label.pack(padx=5,pady=5,side=ctk.TOP)
        ctk.CTkButton(self.nav_frame, text="Border Color", command=self.set_border_color).pack(padx=5,pady=5,side=ctk.TOP)
        self.border_color_label = ctk.CTkLabel(self.nav_frame, text="", bg_color='white', width=30)
        self.border_color_label.pack(padx=5,pady=5,side=ctk.TOP)
        ctk.CTkButton(self.nav_frame, text="Border Width", command=self.set_border_width).pack(padx=5,pady=5,side=ctk.TOP)
        self.spinbox = FloatSpinbox(self.nav_frame, width=150, step_size=1, command=self.set_border_width)
        self.spinbox.pack(padx=5,pady=5,side=ctk.TOP)

        self.appearance_mode_optionemenu = ctk.CTkOptionMenu(self.nav_frame,
                                                               values=["Light", "Dark", "System"],
                                                               command=self.change_appearance_mode_event)
        self.appearance_mode_optionemenu.set("Dark")
        self.appearance_mode_optionemenu.pack(padx=5,pady=5,side=ctk.BOTTOM)
        self.appearance_mode_label = ctk.CTkLabel(self.nav_frame, text="Appearance Mode:", anchor="w")
        self.appearance_mode_label.pack(padx=5,pady=5,side=ctk.BOTTOM)

        # create canvas
        self.canvas = tk.Canvas(self, bg="white")
        self.canvas.grid(row=0, column=1, sticky="nsew")
        self.canvas.grid_columnconfigure(0, weight=1)

        self.canvas.bind("<Button-1>", self.on_click)
        self.canvas.bind("<B1-Motion>", self.on_drag)

        # Add test shape
        # self.rect = self.canvas.create_rectangle(80, 30, 140, 150, fill="blue")

    # Mouse events
    def on_click(self, event):
        selected = self.canvas.find_overlapping(event.x - 10, event.y - 10, event.x + 10, event.y + 10)
        if selected:
            self.canvas.selected = selected[-1]  # select the top-most item
            self.canvas.startxy = (event.x, event.y)
            # print(self.canvas.selected, self.canvas.startxy)
        else:
            self.canvas.selected = None

    def on_drag(self, event):
        if self.canvas.selected:
            # calculate distance moved from last position
            dx, dy = event.x - self.canvas.startxy[0], event.y - self.canvas.startxy[1]
            # move the selected item
            self.canvas.move(self.canvas.selected, dx, dy)
            # update last position
            self.canvas.startxy = (event.x, event.y)

    def create_rect(self):
        self.canvas.create_rectangle(80, 30, 140, 150, fill="blue")

    def create_oval(self):
        self.canvas.create_oval(80, 30, 140, 150, fill="yellow")

    def create_triangle(self):
        points = [50,100,100,25,150,100]
        self.canvas.create_polygon(points, fill="green")

    def create_line(self):
        self.canvas.create_line(80, 30, 140, 150, width=3)

    def set_fill_color(self):
        selected = self.canvas.selected
        color = colorchooser.askcolor()
        color_hex = color[1]
        self.canvas.itemconfig(selected, fill=color_hex)
        self.fill_color_label.configure(bg_color=color_hex)

    def set_border_color(self):
        selected = self.canvas.selected
        color = colorchooser.askcolor()
        color_hex = color[1]
        self.canvas.itemconfig(selected, outline=color_hex)
        self.border_color_label.configure(bg_color=color_hex)

    def set_border_width(self):
        selected = self.canvas.selected
        self.canvas.itemconfig(selected, width=self.spinbox.get())


    @staticmethod
    def change_appearance_mode_event(new_appearance_mode: str):
        ctk.set_appearance_mode(new_appearance_mode)


if __name__ == "__main__":
    app = App()
    app.mainloop()
