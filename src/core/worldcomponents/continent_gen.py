import random
import uuid
import worldcomponents.settlement_gen as settlement_gen

SETTLEMENTS_PER_CONTINENT = 10  # Number of settlements per continent

class Continent:
    def __init__(self, name, area, climate, settlements):
        self.id = str(uuid.uuid4())  # Generate a unique identifier
        self.name = name
        self.area = area  # Area in square kilometers
        self.climate = climate
        self.settlements = settlements

    def __repr__(self):
        return f"Continent(id={self.id}, name={self.name}, area={self.area}, climate={self.climate}, settlements={self.settlements})"

    def to_json(self):
        """Return the continent object in a JSON-appropriate format."""
        return {
            "id": self.id,
            "name": self.name,
            "area": self.area,
            "climate": self.climate,
            "settlements": [settlement.to_json() for settlement in self.settlements]
        }

def generate_random_continent():
    names = ["Aetheria", "Drakoria", "Sylvaris", "Ignis", "Aquatica"]
    climates = ["Temperate", "Tropical", "Arid", "Polar", "Mediterranean"]

    name = random.choice(names)
    area = random.randint(100000, 10000000)  # Random area between 100,000 and 10,000,000 square kilometers
    climate = random.choice(climates)
    settlements = [settlement_gen.generate_random_settlement() for _ in range(random.randint(5, SETTLEMENTS_PER_CONTINENT))]

    return Continent(name, area, climate, settlements)

# Example usage
if __name__ == "__main__":
    random_continent = generate_random_continent()
    print(random_continent)
    print(random_continent.to_json())