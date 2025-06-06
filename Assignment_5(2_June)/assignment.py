# https://api.nobelprize.org/v1/prize.json

import json
import numpy as np


with open("prize.json", "r", encoding="utf-8") as file:
    data = json.load(file)

#  fix the logic of prize count per year
print("Prize count per year\n")
prizesPerYear = {}
for prize in data["prizes"]:
    if "laureates" in prize:
        prizesPerYear[prize["year"]] = prizesPerYear.get(prize["year"], 0) + len(prize["laureates"])
print(prizesPerYear)

#  Total years present : 
print("\nTotal unique years present in the data\n")
years = [prize["year"] for prize in data["prizes"]]
years_array = np.array(years)
unique_years = np.unique(years_array)
print(unique_years)

#  Total prizes awarded : 
totalPrizesAwarded = 0

for val in prizesPerYear.values():
    totalPrizesAwarded = totalPrizesAwarded + val

print(f"\nTotal prizes awarded: {totalPrizesAwarded}")

#  Total Laurates Honoured : 

print(f"\nTotal Laurates Honoured: {len(data["prizes"])}\n")

#  Total unique categories : 

categories = [ prize["category"] for prize in data["prizes"]]
unique_catagories = np.unique(categories)
print(f"Total categories : {unique_catagories}")