import random
import uuid
import worldcomponents.people_gen as people_gen

PEOPLE_PER_BUILDING = 2

class Building:
    def __init__(self, name, use, floors, location, people):
        self.id = str(uuid.uuid4())  # Generate a unique identifier
        self.name = name
        self.use = use
        self.floors = floors
        self.location = location
        self.people = people  

    def __repr__(self):
        return f"Building(id={self.id}, name={self.name}, use={self.use}, floors={self.floors}, location={self.location}, people={self.people})"

    def to_json(self):
        """Return the building object in a JSON-appropriate format."""
        return {
            "id": self.id,
            "name": self.name,
            "use": self.use,
            "floors": self.floors,
            "location": self.location,
            "people": [person.to_json() for person in self.people]
        }

def generate_random_building():
    names = ["The Golden Inn", "Dragon's Rest", "Silver Shoppe", "Oakwood Manor", "The Rusty Hammer"]
    uses = ["Tavern", "Shop", "Hotel", "House", "Workshop"]
    locations = ["New York", "London", "Tokyo", "Paris", "Sydney"]

    name = random.choice(names)
    use = random.choice(uses)
    floors = random.randint(1, 10)  # Random number of floors between 1 and 10
    location = random.choice(locations)
    people = [people_gen.generate_random_person() for _ in range(random.randint(1, PEOPLE_PER_BUILDING))]

    return Building(name, use, floors, location, people)

# Example usage
if __name__ == "__main__":
    random_building = generate_random_building()
    print(random_building)
    print(random_building.to_json())
