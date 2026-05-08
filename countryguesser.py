import random
import json
from typing import Any

with open('countries.json', 'r', encoding='utf-8') as f:
    countries = json.load(f)

used_countries = set()

user_lives = 3
user_points = 0


def get_random_country_letter():
    return random.choice(list(countries.keys()))

# ----- main game loop ----- #

while True:

    random_letter = get_random_country_letter()
    print()
    print(f"Buchstabe: {random_letter}")
    print()
    user_input = input("Land eingeben: ").strip()

   #richtiger Anfangsbuchstabe
    if not user_input or user_input[0].lower() != random_letter.lower():
        print()
        print("Wrong starting letter. -1 Live.")
        

    #existiert das Land
    elif user_input not in countries[random_letter]:
        print()
        print("Country does not exist. -1 Live.")

    #bereits benutzt
    elif user_input in used_countries:
        print()
        print("Country already guessed. -1 Live.")

    # Alles korrekt
    else:
        print()
        print("Correct Guess. +1 Point.")
        user_points += 1
        used_countries.add(user_input)
    
    print(f"Lives:{user_lives} Points:{user_points}")

    # Leben abziehen bei Fehler
    if (
        not user_input
        or user_input[0].lower() != random_letter.lower()
        or user_input not in countries[random_letter]
        or user_input in used_countries and user_input not in used_countries
    ): user_lives=user_lives-1

    if user_lives==0:
        break
        
    
print(f"Hou have lost. You got {user_points} Points.")
user_lives