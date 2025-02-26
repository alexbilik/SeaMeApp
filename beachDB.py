import json
from dataclasses import dataclass
from typing import List


@dataclass
class Beach:
    beach_name: str
    city: str
    wheelchair_accessible: bool
    latitude: float
    longitude: float


class BeachDB:
    def __init__(self, json_file: str):
        self.beaches: List[Beach] = []
        self.load_data(json_file)

    def load_data(self, json_file: str):
        """Load data from the JSON file into the beaches list."""
        try:
            with open(json_file, 'r', encoding='utf-8') as file:
                data = json.load(file)
                for entry in data:
                    beach = Beach(
                        beach_name=entry.get("beach_name", ""),
                        city=entry.get("city", ""),
                        wheelchair_accessible=entry.get("wheelchair_accessible", False),
                        latitude=entry.get("location", {}).get("latitude", 0.0),
                        longitude=entry.get("location", {}).get("longitude", 0.0)
                    )
                    self.beaches.append(beach)
        except Exception as e:
            print(f"An error occurred while loading data: {e}")

    def get_all_beaches(self) -> List[Beach]:
        """Return the list of all beaches."""
        return self.beaches


# Example usage:
if __name__ == "__main__":
    db = BeachDB("database/sample_db.json")
    for beach in db.get_all_beaches():
        print(beach)
