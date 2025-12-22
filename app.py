import requests
import tkinter as tk

def AmiiboAPI(amiibo:str):
    response = requests.get(f"https://www.amiiboapi.com/api/amiibo/?name={amiibo.lower()}")
    if response.status_code != 200:
        print("Error fetching data!")
        return None
    
    data = response.json()

    return data["amiibo"]

my_amiibo = AmiiboAPI("Kirby")

window = tk.Tk()
window.title("Message Reverser")
window.geometry("400x250")
window.resizable(False, False)

window.mainloop()
print(my_amiibo)