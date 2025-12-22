import tkinter as tk
from PIL import Image, ImageTk

window = tk.Tk()
window.title("unc")

image = Image.open("arab-money.png") # open image file
photo = ImageTk.PhotoImage(image) # convert for Tkinter

label = tk.Label(window, image=photo)
label.pack(padx=20, pady=20)

label.image = photo
window.mainloop()