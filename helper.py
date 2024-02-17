import pandas as pd
import requests

def fetch_data(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Request failed with status code {response.status_code}")
        
def get_restuarants(data):
    restuarant_list = []

    for page in data:
        for restaurant in page['restaurants']:
            restuarant_list.append(restaurant)
    
    return restuarant_list