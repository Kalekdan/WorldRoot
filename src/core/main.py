import worldcomponents.continent_gen as continent_gen
import json
print(json.dumps(continent_gen.generate_random_continent().to_json(), indent=4))