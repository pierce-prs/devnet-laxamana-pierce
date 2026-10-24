import random
import requests


random_id = random.randint(1, 1025)


url = f"https://pokeapi.co/api/v2/pokemon/{random_id}"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
     
    pokemon_name1 = data["name"].capitalize()
    pokemon_name2 = data["name"].capitalize()
    pokemon_name3= data["name"].capitalize()
    pokemon_name4 = data["name"].capitalize()
    pokemon_name5 = data["name"].capitalize()
    height = data["height"]
    weight = data["weight"]

    def play_game():

        print("=== Who's the Pokemon? ===")

        print(f"Pokémon 1: {pokemon_name1}") #Randomize 5 Pokemons
        print(f"Pokémon 2: {pokemon_name2}")
        print(f"Pokémon 3: {pokemon_name3}")
        print(f"Pokémon 4: {pokemon_name4}")
        print(f"Pokémon 5: {pokemon_name5}")

        print(f"ID: {random_id}")
        print(f"Height: {height}, Weight: {weight}")

        print(input("Guess The Pokemon: "))
 

play_game()
