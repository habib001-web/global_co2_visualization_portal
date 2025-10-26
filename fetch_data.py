#!/usr/bin/env python3
"""
Fetch and process NOAA Global CO2 Monthly Mean Data
"""

import json
import urllib.request
from statistics import mean

# Fetch data from NOAA
url = "https://gml.noaa.gov/webdata/ccgg/trends/co2/co2_mm_mlo.json"
headers = {
    'User-Agent': 'NOAA-CO2-Data-Fetcher/1.0 (Educational Project; Python/urllib)'
}

req = urllib.request.Request(url, headers=headers)
with urllib.request.urlopen(req) as response:
    raw_data = json.loads(response.read().decode())

# Parse and filter data
co2_data = raw_data.get('co2', [])
filtered_values = []

for entry in co2_data:
    year, month, value = entry[0], entry[1], entry[2]
    
    # Filter: year >= 2010 and value is numeric (not -99.99 which indicates missing)
    if year >= 2010 and isinstance(value, (int, float)) and value > 0:
        filtered_values.append({
            'year': year,
            'month': month,
            'value': value
        })

# Calculate statistics
max_entry = max(filtered_values, key=lambda x: x['value'])
min_entry = min(filtered_values, key=lambda x: x['value'])
average_value = round(mean([x['value'] for x in filtered_values]), 2)

# Create output structure
output = {
    "dataset": "NOAA CO2 Monthly Mean",
    "max": {
        "val": max_entry['value'],
        "year": max_entry['year'],
        "month": max_entry['month']
    },
    "min": {
        "val": min_entry['value'],
        "year": min_entry['year'],
        "month": min_entry['month']
    },
    "average": average_value
}

# Save to data.json
with open('data.json', 'w') as f:
    json.dump(output, f, indent=2)

print(f"Data saved to data.json")
print(f"Max: {max_entry['value']} ppm ({max_entry['year']}-{max_entry['month']:02d})")
print(f"Min: {min_entry['value']} ppm ({min_entry['year']}-{min_entry['month']:02d})")
print(f"Average: {average_value} ppm")