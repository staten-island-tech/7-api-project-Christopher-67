import requests
import tkinter as tk
from tkinter import ttk
from PIL import ImageTk, Image
from io import BytesIO

def AmiiboAPI(amiibo:str):
    link = f"https://www.amiiboapi.com/api/amiibo/?name={amiibo.lower()}"
    
    response = requests.get(link)
    if response.status_code != 200:
        print("Error fetching data!")
        return None

    data = response.json()

    return data["amiibo"]

def get_url_link(amiibo:str, amiibo_id:int):
         return AmiiboAPI(amiibo)[amiibo_id - 1].get("image")

class WebImage:
     def __init__(self,url):
          u = requests.get(url)
          self.image = ImageTk.PhotoImage(Image.open(BytesIO(u.content)))
          
     def get(self):
          return self.image

my_amiibo = AmiiboAPI("mario")

window = tk.Tk()
window.title("unc")

img = WebImage(my_amiibo[0]["image"]).get()
label = tk.Label(window, image=img)
label.image = img
label.pack(padx=50, pady=50)

name_var = tk.StringVar()
char_var = tk.StringVar()
series_var = tk.StringVar()
game_var = tk.StringVar()
type_var = tk.StringVar()

info_frame = tk.Frame(window)
info_frame.pack(anchor="w", padx=20)

tk.Label(info_frame, textvariable=name_var).pack(anchor="w")
tk.Label(info_frame, textvariable=char_var).pack(anchor="w")
tk.Label(info_frame, textvariable=series_var).pack(anchor="w")
tk.Label(info_frame, textvariable=game_var).pack(anchor="w")
tk.Label(info_frame, textvariable=type_var).pack(anchor="w")


choices = [str(i) for i in range(1, len(my_amiibo) + 1)]
dropdown = ttk.Combobox(window, values=choices, width=5)
dropdown.current(0)
dropdown.place(relx=0, rely=0, anchor="nw")
label.image = img

def update_image(event=None):
    amiibo_id = int(dropdown.get()) - 1
    data = my_amiibo[amiibo_id]

    new_img = WebImage(data["image"]).get()
    label.config(image=new_img)
    label.image = new_img

    name_var.set(f"Name: {data['name']}")
    char_var.set(f"Character: {data['character']}")
    series_var.set(f"Amiibo Series: {data['amiiboSeries']}")
    game_var.set(f"Game Series: {data['gameSeries']}")
    type_var.set(f"Type: {data['type']}")

dropdown.bind("<<ComboboxSelected>>", update_image)

update_image()

window.mainloop()
print(my_amiibo)