import csv
import json
from pprint import pprint

EINSTEIN = {
    "birthplace": "Germany",
    "name": "Albert",
    "surname": "Einstein",
    "born": "1879-03-14",
    "category": "physics",
    "motivation": "for his services to Theoretical Physics...",
}

einstein_json = json.dumps(EINSTEIN) #DUMP creates a json file 
back_to_dict = json.loads(einstein_json) #turns json back into dictionary
print(einstein_json)
pprint(back_to_dict)

#creates a list of dictionaries
with open("laureates.csv", "r") as f:
    reader = csv.DictReader(f)
    laureates = list(reader)

# turning them into json file - to be found later as laureates.json
with open("laureates.json", "w") as f:
    json.dump(laureates, f, indent=2)
