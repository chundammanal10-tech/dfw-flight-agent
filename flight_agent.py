import json
import os

# (Inside your script where you gather your flight deals list)
deals = [
    {"Destination": "New Orleans (MSY)", "Price": "$76 RT", "Airline": "Spirit/Frontier"},
    {"Destination": "Atlanta (ATL)", "Price": "$56 RT", "Airline": "Frontier"},
    {"Destination": "Denver (DEN)", "Price": "$123 RT", "Airline": "Frontier"}
]

# Ensure a data directory exists
os.makedirs("data", exist_ok=True)

# Save deals to a JSON file that the dashboard will read
with open("data/deals.json", "w") as f:
    json.dump(deals, f, indent=4)

print("Flight deals saved to data/deals.json successfully!")
