import requests
import tkinter as tk
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

img = WebImage(get_url_link("mario", 8)).get()

label = tk.Label(window, image=img)
label.pack(padx=20, pady=20)
window.mainloop()
print(my_amiibo)