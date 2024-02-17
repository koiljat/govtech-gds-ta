import json
import requests
import logging

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')

def fetch_data(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        logging.info("JSON Data fetched successfully")
        return response.json()
    except requests.HTTPError as http_err:
        logging.error("HTTP error occurred: %s", http_err)
        raise
    except Exception as err:
        logging.error("An error occurred: %s", err)
        raise

        
def get_restuarants(data):
    '''Get the restaurants from the given data.'''
        
    restuarant_list = []

    for page in data:
        for restaurant in page['restaurants']:
            restuarant_list.append(restaurant)
            
    return restuarant_list


## This function will only be used if app is unable to fetch the data from the URL.
def read_json(file_name):
    '''Read the JSON file and return the data.'''
    try:
        with open(file_name, 'r') as file:
            data = json.load(file)
        return data
    except Exception as e:
        logging.error("An error occurred while reading the JSON file")
        raise