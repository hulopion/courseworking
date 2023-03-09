import tkinter
import customtkinter
from app import *

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

app = customtkinter.CTk()
app.geometry("400x240")

def register_button():
    register()
    
def login_button():
    login()

button = customtkinter.CTkButton(master=app,
                                 width=120,
                                 height=32,
                                 border_width=0,
                                 corner_radius=8,
                                 text="Register",
                                 command=register_button)
button.place(relx=0.75, rely=0.8, anchor=tkinter.CENTER)

button = customtkinter.CTkButton(master=app,
                                 width=120,
                                 height=32,
                                 border_width=0,
                                 corner_radius=8,
                                 text="Login",
                                 command=login_button)
button.place(relx=0.25, rely=0.8, anchor=tkinter.CENTER)

app.mainloop()
