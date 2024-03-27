import tkinter as tk
from tkinter import PhotoImage
from ttkbootstrap import Style

def toggle_theme():
    global dark_mode
    dark_mode = not dark_mode
    if dark_mode:
        style.theme_use('darkly')
        toggle_button.config(image=light_image)
    else:
        style.theme_use('flatly')
        toggle_button.config(image=dark_image)

if __name__ == "__main__":
    root = tk.Tk()
    style = Style()
    dark_mode = False

    # Load images for dark mode and light mode buttons
    dark_image = PhotoImage(file="../icons/dark_mode.png").subsample(2)  # Adjust subsample factor as needed
    light_image = PhotoImage(file="../icons/light_mode.png").subsample(2)  # Adjust subsample factor as needed

    # Toggle button for dark mode
    toggle_button = tk.Button(root, command=toggle_theme, relief="flat", bd=0, bg='white', image=dark_image)
    toggle_button.place(x=root.winfo_screenwidth()-dark_image.width(), y=root.winfo_screenheight()-dark_image.height(), anchor="se")

    root.mainloop()
