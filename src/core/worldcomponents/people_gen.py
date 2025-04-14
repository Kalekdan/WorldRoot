import random
import uuid

class Person:
    def __init__(self, name, age, birthplace, species):
        self.id = str(uuid.uuid4())  # Generate a unique identifier
        self.name = name
        self.age = age
        self.birthplace = birthplace
        self.species = species

    def __repr__(self):
        return f"Person(id={self.id}, name={self.name}, age={self.age}, birthplace={self.birthplace}, species={self.species})"

    def to_json(self):
        """Return the person object in a JSON-appropriate format."""
        return {
            "id": self.id,
            "name": self.name,
            "age": self.age,
            "birthplace": self.birthplace,
            "species": self.species
        }

def generate_random_person():
    names = ["Alice", "Bob", "Charlie", "Diana", "Eve"]
    birthplaces = ["New York", "London", "Tokyo", "Paris", "Sydney"]
    species_list = ["Human", "Elf", "Dwarf", "Orc", "Halfling"]

    name = random.choice(names)
    age = random.randint(1, 100)
    birthplace = random.choice(birthplaces)
    species = random.choice(species_list)

    return Person(name, age, birthplace, species)
