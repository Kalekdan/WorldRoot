import random
import uuid
import worldcomponents.building_gen as building_gen

BUILDINGS_PER_SETTLEMENT = 5  # Number of buildings per city

class Settlement:
    def __init__(self, name, population, region, landmarks, buildings):
        self.id = str(uuid.uuid4())  # Generate a unique identifier
        self.name = name
        self.population = population
        self.region = region
        self.landmarks = landmarks
        self.buildings = buildings

    def __repr__(self):
        return f"Settlement(id={self.id}, name={self.name}, population={self.population}, region={self.region}, landmarks={self.landmarks}, buildings={self.buildings})"

    def to_json(self):
        """Return the settlement object in a JSON-appropriate format."""
        return {
            "id": self.id,
            "name": self.name,
            "population": self.population,
            "region": self.region,
            "landmarks": self.landmarks,
            "buildings": [building.to_json() for building in self.buildings]
        }

def generate_random_settlement():
    names = ["Eldoria", "Rivermouth", "Ironhaven", "Stormhold", "Sunspire"]
    regions = ["Northern Plains", "Eastern Highlands", "Western Coast", "Southern Desert", "Central Forest"]
    landmark_options = [
        "Grand Cathedral", "Ancient Ruins", "Royal Palace", "Market Square", "Tower of Mages"
    ]

    name = random.choice(names)
    population = random.randint(1000, 1000000)  # Random population between 1,000 and 1,000,000
    region = random.choice(regions)
    landmarks = random.sample(landmark_options, random.randint(1, 3))  # Randomly select 1-3 landmarks
    buildings = [building_gen.generate_random_building() for _ in range(random.randint(1, BUILDINGS_PER_SETTLEMENT))]

    return Settlement(name, population, region, landmarks, buildings)