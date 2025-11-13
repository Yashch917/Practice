#random module in python is a built-in module that provides functions for generating random numbers and making random selections. It is commonly used in various applications such as simulations, games, and statistical sampling.
import random
print("Random Number between 0 and 0.1:",random.random())  # Generates a random float between 0.0 and 1.0

print("Random Integer between 1 and 10:",random.randint(1,10))  # Generates a random integer between 1 and 10 (inclusive)

print("Random Float between 1.5 and 2.5:",random.uniform(1.5,2.5))  # Generates a random float between 1.5 and 2.5

direction = ['North', 'South', 'East', 'West','Ghatkopar', 'Vikhroli', 'Kanjurmarg', 'Bhandup', 'Mulund', 'Thane', 'Dombivli', 'Kalyan', 'Ulhasnagar', 'Badlapur', 'Vasai', 'Nallasopara', 'Virar','Pune']
print("Random Choice from a list:",random.choice(direction))  # Randomly selects an item from a list

card=['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
random.shuffle(card)
print("Random Sample of 5 cards:",card)  # Randomly selects unique items from a list

dictionary = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
random.shuffle(list(dictionary))
print("Shuffled Dictionary Keys:",list(dictionary))  # Shuffles the keys of a dictionary