import requests
from pprint import pprint

def fetch_rolimons_data():
    url = "https://www.rolimons.com/itemapi/itemdetails"
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers)
    return response.json()

def parse_item(item_id, item_data):
    """Parse the item array into a structured dictionary"""
    return {
        "id": item_id,
        "name": item_data[0],
        "short_name": item_data[1] if item_data[1] else None,
        "rap": item_data[2] if item_data[2] != -1 else None,
        "value": item_data[3] if item_data[3] != -1 else None,
        "demand": item_data[6] if item_data[6] != -1 else None,
        "trend": item_data[7] if item_data[7] != -1 else None,
        "projected": item_data[8] if item_data[8] != -1 else None,
        "hyped": item_data[9] if item_data[9] != -1 else None,
        "rare": item_data[10] if len(item_data) > 10 and item_data[10] != -1 else None
    }



# Main execution
data = fetch_rolimons_data()
items_dict = data.get("items", {})

# Parse all items
parsed_items = [parse_item(item_id, item_data) 
               for item_id, item_data in items_dict.items()]

# Display results
print(f"Total items: {len(parsed_items)}")