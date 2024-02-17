import pandas as pd
import requests
from helper import *
from task1a import *

## Assumption: The file is not given and needs to read from the URL

URL = "https://raw.githubusercontent.com/Papagoat/brain-assessment/main/restaurant_data.json"

## Set up

data = fetch_data(URL)

## Question 1

country_df = pd.read_excel('Country-Code.xlsx')
restuarant_list = get_restuarants(data)
restuarant_df = pd.DataFrame(get_details(restuarant_list), columns=columns)
final_restuarant_df = map_replace(restuarant_df, 'Country', country_df)
final_restuarant_df.to_csv("restaurants.csv")

# ## Question 2

events_columns = ['Event Id', 'Restaurant Id', 'Restaurant Name', 'Photo URL', 'Event Title', 'Event Start Date', 'Event End Date']

def get_events(restuarant_list):
    result = []
    
    for entry in restuarant_list:
        restaurant = entry.get('restaurant', {})
        
        restaurant_id = restaurant.get('R', {}).get('res_id', "NA")
        
        restaurant_name = restaurant.get('name', "NA")
        
        zomato_events = restaurant.get('zomato_events', [])
        
        for item in zomato_events:
            event = item.get('event', {})
            
            event_id = event.get('event_id', "NA")
            
            photos = event.get('photos', [])
            
            photo_URL = "NA"
            
            for photo in photos:
                photo_URL = photo.get('photo', {}).get('URL', "NA")
            
            event_title = event.get('title', "NA").strip()
            
            event_start_date = event.get('start_date', "NA")
            
            event_end_date = event.get('end_date', "NA")
            
            result.append([event_id, restaurant_id, restaurant_name, photo_URL, event_title, event_start_date, event_end_date])
    
    return result
        

event_df = pd.DataFrame(get_events(restuarant_list), columns=events_columns)

event_df

event_df['Event Start Date'] = pd.to_datetime(event_df['Event Start Date'])
filtered_event_df = event_df[(event_df['Event Start Date'] >= '2019-04-01') & (event_df['Event Start Date'] <= '2019-04-30')]

filtered_event_df.to_csv('restaurant_events.csv')
# ## Question 3

def get_ratings(restuarant_list):
    results = []
    
    for entry in restuarant_list:
        restaurant = entry.get('restaurant', {})
        
        user_rating = restaurant.get('user_rating', {})
        
        rating_text = user_rating.get('rating_text', "NA")
        aggregate_rating = user_rating.get('aggregate_rating', "NA")
        
        results.append([rating_text, aggregate_rating])
        
    return results

ratings_df = pd.DataFrame(get_ratings(restuarant_list), columns=['rating_text', 'aggregate_rating'])
target_ratings = ['Excellent', 'Very Good', 'Good', 'Average', 'Poor']
filtered_ratings = ratings_df[ratings_df['rating_text'].isin(target_ratings)]

filtered_ratings['aggregate_rating'] = pd.to_numeric(filtered_ratings['aggregate_rating'], errors='coerce')


grouped_ratings = filtered_ratings.groupby('rating_text').agg({'aggregate_rating': ['min', 'max']})
grouped_ratings = grouped_ratings.reset_index()
grouped_ratings['rating_text'] = pd.Categorical(grouped_ratings['rating_text'], categories=target_ratings, ordered=True)
sorted_ratings = grouped_ratings.sort_values('rating_text')

sorted_ratings


