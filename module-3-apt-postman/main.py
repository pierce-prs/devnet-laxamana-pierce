
import random
import requests

def normalize_name(name):

    return "".join(char.lower() for char in name if char.isalnum())


def play_game():
    print("=== Who's That Pokémon? ===")
    print("Guess the Pokémon using the clues!")
    print("There are 5 rounds. Let's play!\n")

    score = 0

    
    random_ids = random.sample(range(1, 1026), 5)

    for round_number, random_id in enumerate(random_ids, start=1):
        url = f"https://pokeapi.co/api/v2/pokemon/{random_id}"

        try:
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            data = response.json()

        except requests.RequestException:
            print(f"Round {round_number}: Could not load Pokémon.")
            continue

        pokemon_name = data["name"]
        types = ", ".join(
            pokemon_type["type"]["name"].capitalize()
            for pokemon_type in data["types"]
        )

       
        height = data["height"] / 10
        weight = data["weight"] / 10

        
        print(f"Type: {types}")
        print(f"Height: {height:.1f} meters")
        print(f"Weight: {weight:.1f} kilograms")

        guess = input("Guess the Pokémon: ").strip()

        if normalize_name(guess) == normalize_name(pokemon_name):
            print("Correct! You got it! 🎉")
            score += 1
        else:
            correct_name = pokemon_name.replace("-", " ").title()
            print(f"Wrong! The Pokémon was {correct_name}.")

        print(f"Score: {score}\n")

    print("=== Game Over! ===")
    print(f"Your final score: {score}/5")

    if score == 5:
        print("Perfect score! Pokémon Master!")
    elif score >= 3:
        print("Great job, Trainer!")
    else:
        print("Keep practicing, Trainer!")


play_game()
