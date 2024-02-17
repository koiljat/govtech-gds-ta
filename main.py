import pandas as pd
from helper import *
from task1.task1a import *
from task1.task1b import *
from task1.task1c import *

URL = "https://raw.githubusercontent.com/Papagoat/brain-assessment/main/restaurant_data.json"

## Assumption: The file is not given and needs to read from the URL

if __name__ == "__main__":
    ## Set up
    
    data = fetch_data(URL)
    country_df = pd.read_excel('Country-Code.xlsx')

    ## Question 1
    
    restuarant_list = get_restuarants(data)
    restuarant_df = pd.DataFrame(get_details(restuarant_list), columns=columns)
    final_restuarant_df = map_replace(restuarant_df, 'Country', country_df)
    final_restuarant_df.to_csv("restaurants.csv")

    # ## Question 2

    event_df = pd.DataFrame(get_events(restuarant_list), columns=events_columns)
    filtered_event_df = filter_april(event_df)
    filtered_event_df.to_csv('restaurant_events.csv')

    # ## Question 3

    ratings_df = pd.DataFrame(get_ratings(restuarant_list), columns=['rating_text', 'aggregate_rating'])
    grouped_ratings = filter_and_group_ratings(ratings_df)
    sorted_ratings = grouped_ratings.sort_values('rating_text')

