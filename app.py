import requests

def AmiiboAPI(amiibo:str):
    response = requests.get(f"https://www.amiiboapi.com/api/amiibo/?name={amiibo.lower()}")
    if response.status_code != 200:
        print("Error fetching data!")
        return None
    
    data = response.json()

    return data["amiibo"]

my_amiibo = AmiiboAPI("Kirby")

print(my_amiibo)