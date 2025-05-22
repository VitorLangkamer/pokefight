import requests

def pokemon_info(pokemon_name):
    response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon_name.lower()}/")
    if response.status_code == 200:
        data = response.json()
        print(f"Nome: {data['name'].capitalize()}")
        print(f"ID: {data['id']}")
        print(f"Tipo: {', '.join([type['type']['name'].capitalize() for type in data['types']])}")
    else:
        print("Pokemon não encontrado.")
        
pokemon_info("Pikachu")
