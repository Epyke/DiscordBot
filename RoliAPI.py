import requests
import json
import pprint


url = "https://www.rolimons.com/itemapi/itemdetails"

response = requests.get(url)

if response.status_code == 200:
    data = json.loads(response.text)

    items_dict = data

    for i, (item_id, item_data) in enumerate(items_dict.items()):
        if i >= 5:  # Only show first 5 for demo
            break
            
        # Parse the array according to your structure
        name = item_data[0] if len(item_data) > 0 else "N/A"
        short_name = item_data[1] if len(item_data) > 1 else "N/A"
        rap = item_data[2] if len(item_data) > 2 else -1
        value = item_data[3] if len(item_data) > 3 else -1
        demand = item_data[6] if len(item_data) > 6 else -1
        
        print(f"\nItem ID: {item_id}")
        print(f"Name: {name} ({short_name})")
        print(f"RAP: {rap if rap != -1 else 'N/A'}")
        print(f"Value: {value if value != -1 else 'N/A'}")
        print(f"Demand: {demand if demand != -1 else 'N/A'}")
else:
    print(f"Error: {response.status_code}")