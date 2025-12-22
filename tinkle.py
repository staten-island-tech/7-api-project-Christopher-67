import tkinter as tk
window = tk.Tk()
window.title("unc")

photo = tk.PhotoImage(file="arab-money.png")

label = tk.Label(window, image=photo)
label.pack(padx=20, pady=20)

label.image = photo
window.mainloop()