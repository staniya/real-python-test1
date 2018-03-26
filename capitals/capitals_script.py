import random
from capitals import capitals_dict
 
def capital_game(states, cities):
    while True:
        user_input = input(f"Where is the capital of {states}?: ").lower()
        if user_input == cities.lower():
                print("Correct")
                break
        elif user_input == "exit":
            print(f"The capital of {states} is {cities}")
            print("Goodbye")
            break

states = random.choice(list(capitals_dict.keys()))
cities = capitals_dict[states]
capital_game(states, cities)
