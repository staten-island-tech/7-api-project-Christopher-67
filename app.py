import requests

def BinaryJazz(jazz):
    response = requests.get(f"https://binaryjazz.us/genrenator-api/{jazz.lower()}")
    if response.status_code != 200:
        print("Error fetching data!")
        return None
    
    data = response.json()
    return {
        "instruments": data["instruments"],
        "beats": data["beats"],
        "adjectives": data["adjectives"],
        "prefixes": data["prefixes"],
        "suffixes": data["suffixes"],
        "regions": data["regions"],
        "genres": data["genres"],
    }

pokemon = BinaryJazz("Bulbasaur")
print(pokemon)