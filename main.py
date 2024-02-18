import pandas as pd
from task1.helper import *
from task1.task1a import *
from task1.task1b import *
from task1.task1c import *
import logging

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')


URL = "https://raw.githubusercontent.com/Papagoat/brain-assessment/main/restaurant_data.json"

## Assumption: The file is not given and needs to read from the URL

if __name__ == "__main__":
    logging.info("Starting...")
    try:
        logging.info("Fetching data...")
        data = fetch_data(URL)
        ## data = read_json('data/restaurant_data.json') # Replace the line above with this if you are not able to fetch the data from the URL.
        
    except Exception as e:
        logging.error(f"An error occurred while fetching data: {e}")
        raise

    try:
        logging.info("Reading the Excel file...")
        country_df = pd.read_excel('data/Country-Code.xlsx')
    except Exception as e:
        logging.error(f"An error occurred while reading the Excel file: {e}")
        raise

    try:
        logging.info("Running task 1a")
        restuarant_list = get_restuarants(data)
        restuarant_df = pd.DataFrame(get_details(restuarant_list), columns=columns)
        final_restuarant_df = map_replace(restuarant_df, 'Country', country_df)
        final_restuarant_df.to_csv("restaurants.csv", index=False)
        logging.info("restaurants.csv saved")
        
    except Exception as e:
        logging.error("An error occurred in task 1a")
        raise

    try:
        logging.info("Running task 1b")
        event_df = pd.DataFrame(get_events(restuarant_list), columns=events_columns)
        filtered_event_df = filter_april(event_df)
        filtered_event_df.to_csv('restaurant_events.csv', index=False)
        logging.info("restaurant_events.csv saved")
        
    except Exception as e:
        logging.error("An error occurred in task 1b")
        raise
    
    try:
        logging.info("Running task 1c")
        ratings_df = pd.DataFrame(get_ratings(restuarant_list), columns=['rating_text', 'aggregate_rating'])
        grouped_ratings = filter_and_group_ratings(ratings_df)
        sorted_ratings = grouped_ratings.sort_values('rating_text')
        sorted_ratings = sorted_ratings.reset_index(drop=True)
        logging.info(sorted_ratings)

    except Exception as e:
        logging.error("An error occurred in task 1c")
        raise