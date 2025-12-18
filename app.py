import requests

def BinaryJazz(jazz):
    response = requests.get(f"https://binaryjazz.us/genrenator-api/v1/genre/25{jazz()}")
    if response.status_code != 200:
        print("Error fetching data!")
        return None
    
    data = response.json()
    return {
        "name": data["name"],
        "instruments": data["instruments"],
        "beats": data["beats"],
        "adjectives": data["adjectives"],
        "prefixes": data["prefixes"],
        "suffixes": data["suffixes"],
        "regions": data["regions"],
        "genres": data["genres"],
    }

generate = BinaryJazz("genre")

for key, value in generate.items():
    print(f"{key.title()}: {value}")